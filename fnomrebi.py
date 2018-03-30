import requests
import random
import string
import sys




mob = sys.argv[1]
name = sys.argv[2]
agent = random.choice(open('UserAgents.txt').readlines())
random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
url = "http://simpleapi.info/apps/numbers-info/sync.php?device_id=" + random
headers = {'User-Agent': agent.strip()}
payload = {"data": "{\""+mob+"\":\""+name+"\"}"}
r = requests.post(url,headers=headers, data=payload)
print(r.text)
