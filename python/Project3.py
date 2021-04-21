from bs4 import BeautifulSoup
import smtplib
import time
import requests as rq

URL = ("https://www.amazon.com/Philips-278E1A-Frameless-Speakers-Replacement/dp/B07ZSGR5TM/ref=sr_1_7?dchild=1&keywords=monitor&qid=1618982192&sr=8-7")

print("Enter current price: ")
currentPrice = input()

def get_price():
    html = rq.get(URL, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    #price = [i.get_text() for i in soup.find_all('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})]

    # final_price = ''.join(price)[2:8]
    # final_price = int(final_price.replace(',', ''))

     # if final_price > 248:
      #  send_email()
    p = soup.find("span", {"class": "a-size-medium a color-price priceBlockBuyingPriceString"})
    print(p)
    final_price = currentPrice - new_Price;
    if final_price < 0:
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('howdypardner1245@gmail.com', 'Creation_time1245')

    subject = "Price drop!"
    body = "Check this link: " + URL
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('howdypardner1245@gmail.com', 'howdypardner1245@gmail.com', msg)

    print("Hey, email has been sent!")
    server.quit

#while True:
#    get_price()
#    time.sleep(60)




#data = requests.get(websiteLink).content

#soup = BeautifulSoup(data, 'html.parser')
#p = soup.find("h1", {"class":"product-single__title"})
#print(p.string)
#title = p.string

#d = soup.find("span", attrs={"class":re.compile("product-price__price")})
#print(d.text)
#price = d.text

#print("Item %s has price %s" % (title, price))

