import json
import numpy as np

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    
data_json = data["data"]
data_produk = ""
list_kategori = set()
list_status = set()

for dt in data_json:
    list_kategori.add(dt['kategori'])
    list_status.add(dt['status'])
 
list_kategori =  list(list_kategori)
list_status = list(list_status)

for idx in range(len(data['data'])):
    # id_produk = data['data'][idx]['id_produk']
    nama_produk = data['data'][idx]['nama_produk']
    harga_produk = data['data'][idx]['harga']
    katagori_id = list_kategori.index(data['data'][idx]["kategori"])
    status_id = list_status.index(data['data'][idx]['status'])
    # data_produk += f"({id_produk}, '{nama_produk}', {harga_produk}, {katagori_id}, {status_id}),"
    data_produk += f"('{nama_produk}', {harga_produk}, {katagori_id}, {status_id}),"

data_kategori = list(zip(np.arange(len(list_kategori)), list_kategori)) 
data_status = list(zip(np.arange(len(list_status)), list_status))

data_kategori_str = str(data_kategori[:]).replace("[", "").replace("]", "")
data_status_str = str(data_status[:]).replace("[", "").replace("]", "")
data_produk_str = data_produk[:-1]

print(data_produk_str)
# print(data_kategori_str)
# print(data_status_str)