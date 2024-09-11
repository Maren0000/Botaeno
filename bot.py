import os
from typing import Literal, Optional
import discord
from discord.ext import commands
import screenshot
from dotenv import load_dotenv

import songs

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(os.getenv("BOT_PREFIX"), intents=intents)

@bot.event
async def on_ready():
    await screenshot.startplaywright()
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

@bot.tree.command(name = 'b30', description='Best 30')
async def b30(interaction: discord.Interaction, profile: str) -> None:
    await interaction.response.defer()
    imagebuffer = await screenshot.get_image(profile)
    await interaction.followup.send("Here's this player's Best 30:", file=discord.File(fp=imagebuffer,filename='image.png'))

@bot.tree.command(name = 'songinfo', description='Fetch info about song')
async def songinfo(interaction: discord.Interaction, songname: str, diff: str=None) -> None:
    await interaction.response.defer()
    if diff is None:
        songinfo = await songs.GetSongInfo(songname)
        if songinfo.name is None:
            await interaction.followup.send("Failed to get Info")
        else:
            await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nSong Artist: "+songinfo.artist+
                                            "\nJacket Artist: "+songinfo.cover_artist+
                                            "\nRelease Version: "+songinfo.version,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))
    else:
        songinfo = await songs.GetSongInfo(songname)
        match diff:
            case "i":
                await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nDifficulty (I): " + songinfo.chart_constant_i+
                                            "\nCharter: "+songinfo.charter_i,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))
            case "ii":
                await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nDifficulty (II): " + songinfo.chart_constant_ii+
                                            "\nCharter: "+songinfo.charter_ii,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))
            case "iii":
                await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nDifficulty (III): " + songinfo.chart_constant_iii+
                                            "\nCharter: "+songinfo.charter_iii,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))
            case "iv":
                await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nDifficulty (IV): " + songinfo.chart_constant_iv+
                                            "\nCharter: "+songinfo.charter_iv,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))
            case "iv-a":
                await interaction.followup.send("Song Name: "+songinfo.name+
                                            "\nDifficulty (IV-A): " + songinfo.chart_constant_iv_a+
                                            "\nCharter: "+songinfo.charter_iv_a,
                                            file=discord.File(fp="./web/static/assets/song-covers/"+songinfo.id+".png" ,filename='image.png'))

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

def startbot():
    bot.run(os.getenv("BOT_TOKEN"))