# # receive data to thinkspeak server
import time
import requests
import urllib.request
import urllib
from urllib import request


# # time.sleep(3)
# field1 = str(700)
# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1='+field1)


# filedata =requests.get("https://api.thingspeak.com/channels/1661789/fields/1.json?api_key=BWRV718JS99HRK3N&results=1")

# msg0=filedata.json()['feeds'][-1]['field1']
# print("Channel 1:- ",msg0)

# field2 = str(60.23)
# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field2='+field2)


# tempdata =requests.get("https://api.thingspeak.com/channels/1661789/fields/2.json?api_key=BWRV718JS99HRK3N&results=2")

# msg1=tempdata.json()['feeds'][-1]['field2']
# print("Channel 2:- ",msg1)


# field3 = str(23.19)
# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field3='+field3)

# # https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=2

# # humData =requests.get("https://api.thingspeak.com/channels/1661789/fields/3.json?api_key=BWRV718JS99HRK3N&results=3")
# humData =requests.get("https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=2")


# msg2=humData.json()['feeds'][-1]['field3']
# print("Channel 3:- ",msg2)


# link = "https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=2"

# &field1=10&field2=20&field3=30

# uplink = "https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1=400&field2=20.54&field3=750" # etc. 
uplink = "https://api.thingspeak.com/update?api_key=YYN5LAINXD8Y6Y4A&field1=450"

# # uplink = "https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1=10" # etc. 

# # urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field3='+20)
# urllib.request.urlopen(uplink)

resp = request.urlopen(uplink)
print(resp.code)    # 200 is a good value, 400:bad request, 403:forbidden Request, 404:not found
print(resp.length)
print(resp.peek())
# field1 = str(700)
# field2 = str(60.23)
# field3 = str(80.23)
# time123 = 50
print("Started running")
# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1='+field1)
print("updated filed 1 : 400")
# time.sleep(time123)
# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field2='+field2)
# print("updated filed 2")

# time.sleep(time123)

# urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field3='+field3)
# print("updated filed 3")




# humData1 =requests.get("https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=1")
# msg1=humData1.json()['feeds'][-1]['field1']
# print("Channel 1:- ",msg1)


# humData2 =requests.get("https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=2")
# msg2=humData2.json()['feeds'][-1]['field2']
# print("Channel 2:- ",msg2)


# humData =requests.get("https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N&results=3")
# msg3=humData.json()['feeds'][-1]['field3']
# print("Channel 3:- ",msg3)



# https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1=0

# https://api.thingspeak.com/channels/1661789/fields/1.json?api_key=BWRV718JS99HRK3N&results=2

#####################################################################################
# send data to thinkspeak server


# import urllib.request
# msg=input('Enter your number : ')

# b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field2='+msg)
# print("\nYour message has successfully been sent!")


# https://api.thingspeak.com/update?api_key=42J30P59Q38LHIRY&field1=0


################################################################################################################################################################

# Based on the snippet, I think the issue is your code that is updating the channel is updating one field per update, instead of one update that updates all fields.

# The most efficient code on your device would do a HTTP GET request like this:

# https://api.thingspeak.com/update?api_key=YOUR_API_KEY_HERE&field1=10&field2=20&field3=30, etc. 


'''
ref:

https://community.thingspeak.com/forum/thingspeak-api/channel-feeds-coming-through-as-null-since-adding-fields/



'''