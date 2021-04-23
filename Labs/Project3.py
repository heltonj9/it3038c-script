#Necessary to import smtplib so that we can send an email, and time so we can run the script
#on a timer before it repeats to prevent being kicked from the website for possible DDoS attacking.
#Also import the soup and requests functions from in-class to get the website scanner working.
from bs4 import BeautifulSoup
import smtplib
import time
import requests, re
#Declaring price_Drop as false initially so that the script continues to run until changed
#to true and an email is sent.
price_Drop = False;

#The one thing a user would have to change when wanting to use this script: the page URL. Same script should work
#for any listing on Newegg's website.
URL = ("https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen%205%205600&cm_re=ryzen_5%205600-_-19-113-666-_-Product")

#User enters current listing price so that the console can begin comparing prices. Necessary
#to get the program started without having new prices input into both current price and new price
#each time the cycle runs.
print("Enter current price: ")
currentPrice = input()
print("Current price was %s" % (currentPrice))
#Converting the currentPrice variable from string to int.
currentPrice = int(re.search('[0-9]+',currentPrice).group(0))

#Declaring the process get_price() as a combined entity so that we can have it continue to
#run or stop running depending on one line later.
def get_price():
    data = requests.get(URL).content
    soup = BeautifulSoup(data, 'html.parser')
    new_Price = soup.find('li', {"class":'price-current'}).text
#Converting the new_Price variable from string to int form so we can use it for math.
    new_Price = new_Price.replace('$','')
    new_Price = int(re.search('[0-9]+',new_Price).group(0))
#Displaying in console the logistics of the price search before using it in the script.
    print("New price was %s" % (new_Price))
    final_price = currentPrice - new_Price;
    print ("Price difference was %s" % (final_price))
#Defining the subject "send_email()" and combining the whole process of sending an email 
#so that it will all run under one message later.
    def send_email():
        #Specifying which server to connect to to send the email from. Chose google for this example.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        #Need to log into a gmail account to send emails through this method. I created an account just for this
        #script with no person info on it.
        server.login('howdypardner1245@gmail.com', 'Creation_time1245')
        #Basically just the message to be sent.
        subject = "Price drop!"
        body = "Price of this item has dropped from $%s to $%s. \nCheck this link to check it out: "% (new_Price, currentPrice) + "https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen%205%205600&cm_re=ryzen_5%205600-_-19-113-666-_-Product"
        msg = f"Subject:{subject}\n\n{body}"
        #Receiver, sender, message. Formatting for the subject line and how the message will appear
        server.sendmail('howdypardner1245@gmail.com', 'howdypardner1245@gmail.com', msg)

        print("Hey, email has been sent!")
        #Exit out of google's server, end the script.
        server.quit
        exit();

    #Deciding what to do with the difference in price. If price is same or higher, don't send
    #an email alert and continue to cycle the script. If price is lower, send an email and
    #change price_Drop to true, ending the script.
    if final_price < 0:
        print("Price decrease to %s! Sending email..."% new_Price)
        price_Drop = True;
        send_email()
    elif (final_price == 0):
        print("Price did not change from %s. Retrying..."% new_Price)
        price_Drop = False;
    elif final_price > 0:
        print("Price increase to %s. Uh oh! Retrying..."% new_Price)
        price_Drop = False;

#Setting up the cycle so that the program will keep running, as well as setting how often
#the script will cycle. Currently set to 60 seconds, during testing was able to go down to 0.3
#seconds.
while price_Drop == False:
    get_price()
    time.sleep(60)
