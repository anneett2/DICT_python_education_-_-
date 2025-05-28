import os
import requests
from bs4 import BeautifulSoup
import string


pages = int(input("Скільки сторінок обробити? "))
article_type = input("Введи тип статті (наприклад, News): ").strip()

base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="

import string

for page in range(1, pages + 1):
    dir_name = f"Page_{page}"
    os.makedirs(dir_name, exist_ok=True)
    response = requests.get(base_url + str(page))
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        type_tag = article.find('span', {'data-test': 'article.type'})
        if type_tag and type_tag.text.strip() == article_type:
            link_tag = article.find('a', {'data-track-action': 'view article'})
            if link_tag:
                href = link_tag.get('href')
                article_url = "https://www.nature.com" + href
                article_page = requests.get(article_url)
                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                body = article_soup.find('div', class_='c-article-body')
                if not body:
                    body = article_soup.find('div', class_='article-item__body')  # fallback
                title_tag = article_soup.find('h1')
                if body and title_tag:
                    title = title_tag.text.strip()
                    file_name = title.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_") + ".txt"
                    path = os.path.join(dir_name, file_name)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(body.text.strip())

print("Saved all articles.")
