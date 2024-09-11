import io
from playwright.async_api import async_playwright

async def startplaywright():
    global page
    playwright = await async_playwright().start()
    browser = await playwright.firefox.launch()
    page = await browser.new_page()

async def get_image(userID):
    await page.set_viewport_size({"width": 980, "height": 1695})
    await page.goto('http://localhost:5000/?user='+userID)
    image = await page.screenshot(type="png")
    imagebuffer = io.BytesIO(image)
    imagebuffer.seek(0)
    return imagebuffer
