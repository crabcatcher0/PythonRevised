#facebook Graph API
import requests
import os

url = "https://graph.facebook.com/{}/picture?type=large"

if not "fb_p" in os.listdir():
    os.mkdir("fb_p")
    
    for i in range(4, 20):
        result = requests.get(url.format(i))
        with open("fb_p/{}_img.jpg".format(i), "wb") as file:
            file.write(result.content)