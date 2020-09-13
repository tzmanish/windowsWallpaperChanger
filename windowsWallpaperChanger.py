from requests import get
from os import getcwd
import ctypes

def getWallpaperUrl():
    clientID = "urBKY5E5rNKirQUKPA1ExW6Fj0MLxDhA-NK1Yx_B3og"
    url = "https://api.unsplash.com/photos/random?query=wallpaper&orientation=landscape"
    response = get(url+"&client_id="+clientID)
    return response.json()['urls']['full']

def saveWallpaper(url):
    fileName = "wallpaper.jpg"

    response = get(url)
    with open(fileName, "wb") as f:
        f.write(response.content)

    directory = getcwd()
    imagePath = directory + '\\' + fileName
    return imagePath

def setWallpaper(imagePath):
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE   = 3      #forces instant update
    
    return ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 
        0, 
        imagePath, 
        SPIF_UPDATEINIFILE
    )

if __name__ == "__main__":
    url = getWallpaperUrl()
    imagePath = saveWallpaper(url)
    setWallpaper(imagePath)