import socket, sys

#Need to use command (python .\python\mygetip.py [website URL])

def getHostnameByIP(h):
    try:
        hostname = str(h)   #previously hostname = str(sys.argv[1])
        ip = socket.gethostbyname(hostname)
        print(hostname + " has an IP of " + ip)
    except:
        print("Oops, something is wrong with that host. Run the command with a valid hostname!")

getHostnameByIP(sys.argv[1])