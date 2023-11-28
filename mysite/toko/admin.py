from django.contrib import admin

# Register your models here.
from .models import Kategori
from .models import Produk
from .models import Status

admin.site.register(Kategori)
admin.site.register(Produk)
admin.site.register(Status)