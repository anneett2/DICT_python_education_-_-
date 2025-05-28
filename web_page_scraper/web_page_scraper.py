import requests
from bs4 import BeautifulSoup


url = input("Input the URL:\n> ")
if "imdb.com/title/" not in url:
    print("Invalid movie page!")
else:
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response.status_code != 200:
        print("Invalid movie page!")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.title
        desc_tag = soup.find('meta', {'name': 'description'})

        if title_tag and desc_tag:
            title = title_tag.text.strip()
            description = desc_tag.get('content').strip()
            print({"title": title, "description": description})
        else:
            print("Invalid movie page!")

