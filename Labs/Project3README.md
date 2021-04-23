My Project 3 is a python script mainly utilizing soup, smtplib, and time to scan a website for price updates on an item, and emailing the user a new price every 60 seconds. 

STEPS TO RUNNING Project3.py CORRECTLY

1) Enter the URL. For testing purposes, you can keep the current URL already in the script. Most Newegg listings should work the same just by changing the URL in the script.
2) If you want to change the email used in the file, you do unfortunately have to enter both email address and password to that email. I created a test account just for this script, so feel free to use that to view your received emails (Note that to get my gmail account working, I also had to enable allowing low security applications ability to login.)
3) Run the script. I used Visual Basic and local files stored directly on my C drive and the command "Python C:/it3038c-script/Labs/Project3.py" in terminal, but pretty much just enter your own filepath wherever the file is saved for you with Python in front of it (ex. "Python {filepath})
4) Enter current listing price. It may seem inconvenient, but entering the current listing price the first time around is the best way to get the script started.
5) Receive emails if the price on the product goes down, and enjoy! Also note that upon sending an email, the script will stop, so if you wish to have it look for an even further price drop, you will have to restart the script.
