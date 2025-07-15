import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.co.uk/Pok%C3%A9mon-TCG-Scarlet-Violet-Stellar-Booster/dp/B0DBVGL83N?ref_=ast_sto_dp&th=1")

page = response.text

soup = BeautifulSoup(page, "html.parser")

print(soup.find(id="productTitle").getText().strip())