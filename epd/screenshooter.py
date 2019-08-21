import os
import time
import epd7in5
import subprocess
from PIL import Image

SCREENSHOT = 'screen.png'
DELAY = 5 * 60 * 60
os.environ['DISPLAY'] = ':1'

def takeScreenShot():
    subprocess.call('import -window root ' + SCREENSHOT, shell=True)
    epd = epd7in5.EPD()
    epd.init()
    epd.Clear(0xff)
    image = Image.open(SCREENSHOT)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    epd.sleep()

while True:
    takeScreenShot()
    time.sleep(DELAY)
