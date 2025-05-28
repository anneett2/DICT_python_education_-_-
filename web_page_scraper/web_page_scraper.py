import requests
import string
import os
from bs4 import BeautifulSoup

base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')
saved = []

for article in articles:
    type_tag = article.find('span', {'data-test': 'article.type'})
    if type_tag and type_tag.text.strip() == "News":
        link_tag = article.find('a', {'data-track-action': 'view article'})
        if link_tag:
            href = link_tag.get('href')
            article_url = "https://www.nature.com" + href
            article_page = requests.get(article_url)
            article_soup = BeautifulSoup(article_page.content, 'html.parser')
            body = article_soup.find('div', class_='c-article-body')
            if body:
                title_tag = article_soup.find('h1')
                if title_tag:
                    title = title_tag.text.strip()
                    filename = title.translate(str.maketrans('', '', string.punctuation))
                    filename = filename.replace(' ', '_') + ".txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(body.text.strip())
                    saved.append(filename)

print(f"Saved articles: {saved}")