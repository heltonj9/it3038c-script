import requests, re
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.com/Philips-278E1A-Frameless-Speakers-Replacement/dp/B07ZSGR5TM/ref=sr_1_7?dchild=1&keywords=monitor&qid=1618982192&sr=8-7').content

soup = BeautifulSoup(r, "lxml")

#tags = soup.findAll("a", {"href":re.compile('(allinone)')})
#for a in tags:
#    print(a.get('href'))

p = soup.find("span", {"class": "a-size-medium a-color-price priceBlockBuyingPriceString"})

print(p)