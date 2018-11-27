#importing all needed modules
import requests
import time
from mail_sender import *
import json
import pprint

#funtion to write the latest ip in file
def Write_file_ip(ip):
    file = open("ip_log.txt", "w")
    file.write(ip)
    file.close()

#function to check the ip from icanhazip service
def check_ip():
    try:
        session = requests.Session()
        response = session.get('http://www.icanhazip.com', timeout=10)        
        return (str(response.text))
    except:
        return

#read the last saved ip in file
def read_file_ip():
    try:
        file = open("ip_log.txt", "r")
        last_ip = file.read()
        file.close()
        return (str(last_ip))
    except:
        print("cant find the file")

#get the location of the ip from ipinfo service
def get_location():
    send_url = 'https://ipinfo.io'
    ipinfo_response = requests.get(send_url)
    ipinfo_jason = json.loads(ipinfo_response.text)    
    return (ipinfo_jason)

#infinity loop which will check the ip every 60 seconds
while True:
    ip = check_ip()
    last_ip = read_file_ip()
    print(ip)
    print (last_ip)
    if ip == last_ip:
        print ("equal")
    else:        
        loc = get_location()        
        text = "your ip have been changed to {}\nthanks for using our service\n".format(ip)        
        text+="\n{}\n\nthis app was created by alibigdeli known as blackfox".format(str(loc))
        text+="\n\nclick the link below to see your location:\nhttps://www.google.com/search?q={}".format(loc.get("loc"))
        print(text)        
        #sending the mail with the detail needed
        sendmail("address of the sender","password of sender","reciever address","IP Notifier",text)
        Write_file_ip(ip)
    time.sleep(60)





    
	
