import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.amazon.com/Philips-278E1A-Frameless-Speakers-Replacement/dp/B07ZSGR5TM/ref=sr_1_7?dchild=1&keywords=monitor&qid=1618982192&sr=8-7").content

soup = BeautifulSoup(data, 'html.parser')
#p = soup.find("h1", {"class":"product-single__title"})
#print(p.string)
#title = p.string

d = soup.find_all("span", attrs={"class":re.compile("a-size-medium a-color-price priceBlockBuyingPriceString")})
#print(d.text)
price = d
print(d)
#print("Item has price %s" % (price))

