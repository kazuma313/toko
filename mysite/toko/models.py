from django.db import models

class Kategori(models.Model):
    nama_katagori = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nama_katagori

class Status(models.Model):
    nama_status = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nama_status

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    nama_produk = models.TextField()
    harga = models.IntegerField()
    def __str__(self) -> str:
        return self.nama_produk
    
    
