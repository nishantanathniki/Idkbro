#Main.py
import requests
import time
from keep_alive import keep_alive
from session import login
from Data import data
import random
import os 
print(os.getcwd())
#session = login()

keep_alive()

url = "https://api.thecoinday.app/api/v1/userenergy"

h = {
      "Host": "api.thecoinday.app",
    "content-type": "application/json",
    "cookie": "",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.8.0"
}
l = []
with open("allidtokens.txt","r")as rr:
  l = rr.read().split(",")
#print(login())
j = 0
while(True):
  for i in l:
    if (j==30):
      j=0
    print("Account No ",j)
    while(True):
      try:
        data1 = {"data" : ""}
        data1["data"] = data()
        s = login(i)
        h["cookie"]="session\u003d"+s
     
        r = requests.post(url,headers=h,json=data1).json()
        print(r["message"])
      
        if (r["statuscode"] == 400):
          break
      
      except:
        print("Error")
    j = j+1
  print("Sleeping For 6 Minutes")
  time.sleep(6*60)
