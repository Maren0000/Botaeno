import json
from PIL import Image

class Song:
    id: str = None
    name: str = None
    artist: str = None
    cover_artist: str = None
    level: str = None
    chart_constant_i: str = None
    chart_constant_ii: str = None
    chart_constant_iii: str = None
    chart_constant_iv: str = None
    chart_constant_iv_a: str = None
    charter_i: str = None
    charter_ii: str = None
    charter_iii: str = None
    charter_iv: str = None
    charter_iv_a: str = None
    pack: str = None #not in wiki json
    version: str = None

    async def GetInfo(self, songname):
        filename = "songinfo.json"
        with open(filename, "r", encoding="utf8") as jsondata:
            data = json.load(jsondata)
            for a in data["songs"]:
                if a["id"] == songname:
                    self.id = a["id"]
                    self.name = a["title_localized"]["default"]
                    self.artist = a["artist"]
                    self.cover_artist = a["difficulties"][0]["jacketDesigner"]
                    self.version = a["release_version"]
                    self.chart_constant_i = str(a["difficulties"][0]["ratingReal"])
                    self.chart_constant_ii = str(a["difficulties"][1]["ratingReal"])
                    self.chart_constant_iii = str(a["difficulties"][2]["ratingReal"])
                    self.chart_constant_iv = str(a["difficulties"][3]["ratingReal"])
                    if len(a["difficulties"]) > 4:
                        self.chart_constant_iv_a = str(a["difficulties"][4]["ratingReal"])
                    self.charter_i = a["difficulties"][0]["chartDesigner"]
                    self.charter_ii = a["difficulties"][1]["chartDesigner"]
                    self.charter_iii = a["difficulties"][2]["chartDesigner"]
                    self.charter_iV = a["difficulties"][3]["chartDesigner"]
                    if len(a["difficulties"]) > 4:
                        self.charter_iV = a["difficulties"][4]["chartDesigner"]
        return self


def GetSongInfo(songname):
    song = Song()
    songdata = song.GetInfo(songname)
    return songdata

def GetSongRandom():
    return None

def SongSearchConst(constant):
    return constant

def SongSearchArtist(Artist):
    return Artist

async def GetSongCover(id):
    return Image.open("./web/static/assets/song-covers/"+id+".png")
