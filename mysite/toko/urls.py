from django.urls import path

from . import views

# Lihat tutorial 3 bagian Use templat system

urlpatterns = [
    path('', views.index, name='index'),
    # path('form', views.create_form, name='form'),
    path('produk/<int:produk_id>/', views.produk, name='produk'),
    path('delete/<int:produk_id>', views.delete_produk, name='delete'),
    path('edit/<int:produk_id>', views.edit_form, name='edit'),
    path('update/<int:produk_id>', views.update_produk, name='update'),
    path('add_data', views.addData, name='add_data'),
    
]