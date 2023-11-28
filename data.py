import hashlib
import datetime
import requests
import json

username = ""
password = ""
password_md5 = hashlib.md5(password.encode()).hexdigest()

authload = {'username':username,'password':password_md5}

req = requests.post("https://recruitment.fastprint.co.id/tes/api_tes_programmer", data=authload)
data = req.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


