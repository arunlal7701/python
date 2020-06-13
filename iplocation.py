import requests
import json

ip = []

logFile = open('/var/log/apache2/access.log')
key = "604a43d7a0a1971161d9a6da7194a3c2"

for logLine in logFile:
    
    ipaddress = logLine.split()[0]
    
    
    if ipaddress not in ip:
            
        
        ip.append(ipaddress)
        
for ips in ip:

    



    try:
        url = 'http://api.ipstack.com/{}?access_key={}'.format(ips,key)
        response = requests.get(url)
        geodata = response.json()
        country_name = geodata['country_name']
        country_code = geodata['country_code']
        print('IP is {} and the location is :{:10} {}'.format(ips,country_name,country_code))
    except:
        print('Please enter the valid credentials')
