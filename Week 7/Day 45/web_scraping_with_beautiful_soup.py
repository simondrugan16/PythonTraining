from bs4 import BeautifulSoup

with open("Week 7/Day 45/website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

#print(soup.prettify())

print(soup.a.string)

all_anchor_tags = soup.find_all(name="a")

print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")

print("@@@@@@")
print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)

company_url = soup.select_one(selector="p a").get("href")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)