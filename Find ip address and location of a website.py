#find ip address and location of a website
#created by Jr.vossough
#If you are in Iran, you can send a message to the @Enzo00o ID in Telegram for free access to the Internet 
#first install ip2geotools whit this commad in windows "pip install ip2geotools"
#update your python whit this command  python.exe -m pip install --upgrade pip
import socket
from ip2geotools.databases.noncommercial import DbIpCity

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

url = input("Insert your url:")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key='free')
print("Your IP address :", IP)
print("Your computer name :", hostname)
print("Website IP : ",ip)
print("Website location ")  
print("City : ", response.city)
print("Region : ", response.region)
print("Country : ", response.country)

#if you haven't pip on your windows you can follow this step's:
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.