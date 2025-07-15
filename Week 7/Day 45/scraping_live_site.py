import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

page = response.text

soup = BeautifulSoup(page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

result = list(zip(article_texts, article_upvotes, article_links))

print(result)