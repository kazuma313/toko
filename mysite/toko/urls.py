from django.urls import path

from . import views

# Lihat tutorial 3 bagian Use templat system

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:produk_id>', views.delete_produk, name='delete'),
    path('edit/<int:produk_id>', views.edit_produk, name='edit'),
    path('add_data', views.add_produk, name='add_data'),
]