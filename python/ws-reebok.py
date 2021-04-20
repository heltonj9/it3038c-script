import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://store.crunchyroll.com/collections/new-pre-orders/products/jujutsu-kaisen-yuji-itadori-prize-figure-vol-2").content

soup = BeautifulSoup(data, 'html.parser')
p = soup.find("h1", {"class":"product-single__title"})
#print(p.string)
title = p.string

d = soup.find("span", attrs={"class":re.compile("product-price__price")})
#print(d.text)
price = d.text

print("Item %s has price %s" % (title, price))

