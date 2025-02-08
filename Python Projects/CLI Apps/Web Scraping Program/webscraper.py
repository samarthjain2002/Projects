import requests
from bs4 import BeautifulSoup as bs

github_username = input("Input Github username: ")

url = f"https://github.com/{github_username}"

r = requests.get(url)
soup = bs(r.content, "html.parser")

profile_image = soup.find("a", {"itemprop": "image"}).img["src"]

if profile_image:
    print(profile_image)
else:
    print("User not found or avatar not available.")
