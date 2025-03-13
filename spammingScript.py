#This script is written to level up in discord server(bot function) Please do not use it to disturb other
import requests

payload = {
    "content" : "This is my spamming script" # your spamming content
}

header = { 
  "Authorization" : "Paste your authorization in here" 
   # you need website discord. Press F12. Send some message in discord. 
   # In NetWork, click message. Go to header. Copy the Request URL
   # scroll down to request_header to find authorization
}

for spam in range(10000):
    r = requests.post("Paste your Request URL in here", data = payload, headers = header)

