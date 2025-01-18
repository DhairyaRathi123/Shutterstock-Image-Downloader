from bs4 import BeautifulSoup
import os
import requests

# Original URL
urlint = str(input("provide url"))

# Modify the URL to append "600nw" and ".jpg"
parts = urlint.rsplit('-', 1)
url = f"{parts[0]}-600nw-{parts[1]}.jpg"

# Filename to save the image
filename = "downloaded_image.jpg"

# Fetch the image content
response = requests.get(url, stream=True)

if response.status_code == 200:
    # Save the image locally
    with open(filename, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print(f"Image downloaded successfully as '{filename}'")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")
