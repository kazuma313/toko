import hashlib
import datetime
import requests
import json

result = hashlib.md5("bisacoding-24-11-23".encode())
tanggal = datetime.date.today().strftime('%d-%m-%Y')[:-4]
year =  datetime.date.today().strftime('%d-%m-%Y')[-2:]

username = "tesprogrammer251123C00"
# password = "bisacoding-" + tanggal + year
password = "bisacoding-25-11-23"
password_md5 = hashlib.md5(password.encode()).hexdigest()

authload = {'username':username,'password':password_md5}

req = requests.post("https://recruitment.fastprint.co.id/tes/api_tes_programmer", data=authload)
data = req.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


