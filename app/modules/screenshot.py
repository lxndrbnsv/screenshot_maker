import datetime

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MakeScreenshot:
    def __init__(self, url):
        filename = url.replace(
            "https://", ""
        ).replace(
            ".", "_"
        ).replace(
            "/", "_"
        ) + str(round(datetime.datetime.now().timestamp())) + ".png"

        options = Options()
        options.headless = True
        options.add_argument(
            "--user-agent=Cron"
        )
        browser = webdriver.Chrome(
            executable_path="./webdriver/chromedriver",
            options=options
        )
        browser.set_window_size("1200", "700")
        browser.get(url)
        browser.save_screenshot(filename)
        browser.quit()

        self.filename = filename


class CropScreenshot:
    def __init__(self, filename):
        picture = Image.open(filename)

        resized = picture.resize((1200, 700))
        resized.save(filename)
        picture = resized
        width = picture.size[0]
        height = picture.size[1]

        x1 = 0
        y1 = 0
        x2 = width
        y2 = height - 70

        cropped = picture.crop(
            (x1, y1, x2, y2)
        )
        cropped.save(filename)
