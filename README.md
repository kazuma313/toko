# Toko online menggunakan django

Membuat toko crud menggunakan django

## Database

Database yang saya gunakan berada pada file _toko.sql_. gambar ERD yang saya terapkan berada pada folder _/flow_. file _database.py_ merupakan experiment database postgreSQL menggunakan python. Pada django, untuk database settings berada pada file _/project_name/settings.py_.

### data

data yang saya dapat tersedia dari api yang saya ambil. cara pengambilannya berada pada file _data.py_. data yang telah diambil saya simpan dalam _data.json_.
Data dari file json tersebut diolah untuk agar dapat dilakukan insert ke table database dengan mudah pada file _string_data.py_.

## django

Project mysite memiliki aplikasi yang bernama toko. Django memiliki fitur yang dapat mengnerate form secara otomatis berdasarkan model yang telah dibuat. untuk memfasilitasi generate form tersebut, berada pada file _forms.py_ dan untuk membuat model berada pada file _models.py_. model dan form juga telah difasilitasi fitur untuk melakukan validasi.

## usage

pastikan berada pada folder _/mysite_, module-module telah terinstal dan database telah di buat. jalankan perintah

```
python manage.py runserver
```

## gambar

Berikut adalah gambar pada index

![index](https://raw.githubusercontent.com/kazuma313/toko/main/gambar/home.png)

Berikut adalah gambar form dari django form.

![form](https://raw.githubusercontent.com/kazuma313/toko/main/gambar/form.png)
