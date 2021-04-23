import requests, re
from bs4 import BeautifulSoup
import smtplib
import time

data = requests.get("https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen%205%205600&cm_re=ryzen_5%205600-_-19-113-666-_-Product").content
soup = BeautifulSoup(data, 'html.parser')
#p = soup.find("h1", {"class":"product-single__title"})
#print(p.string)
#title = p.string

print("Enter current price:")
current_price = input();
print("Current price is %s" % )

d = soup.find('li', attrs={"class":re.compile:'price-current'})
#print(d.text)
#print(soup)

print(d.text)
#print("Item has price %s" % (price))

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
