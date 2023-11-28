from django.shortcuts import render, get_object_or_404, redirect 
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Kategori, Status, Produk
from django.http import Http404
from django.urls import reverse
from .forms import ProdukForm
from django.contrib import messages

def index(request):
    status = Status.objects.get(nama_status = "bisa dijual")
    context = {
        'statuss' : status
    }
    return render(request, 'toko/index.html', context)

def produk(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    return render(request, 'toko/produk.html', {'produks': produk})

def addData(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            produk = form.save(commit=False)
            produk.save()
            messages.success(request, "Data Added.")
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, "periksa kembali data anda")
            return render(request, 'toko/form.html', {'form':form}) 
    form = ProdukForm(None)   
    return render(request, 'toko/form.html', {'form':form})
    
def delete_produk(request, produk_id):
    produk = Produk.objects.get(id=produk_id)
    if request.method == "POST":
        produk.delete()
        messages.error(request, "Document deleted.")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'toko/delete_form.html', {'produk':produk})

def edit_form(request, produk_id): 
    instance = get_object_or_404(Produk, id=produk_id)
    form = ProdukForm(request.POST or None, instance=instance)
    if form.is_valid():
        produk = form.save(commit=False)
        produk.save()
        messages.success(request, "Data updated.")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'toko/form.html', {'form': form}) 
 
def update_produk(request, produk_id):
    if request.method == 'POST':
        kategori = request.POST["kategori"]
        status = request.POST["status"]
        nama_produk = request.POST["nama_produk"]
        harga = request.POST["harga"]
        
        produk = Produk.objects.get(id=produk_id)
        produk.nama_produk = nama_produk
        produk.harga = harga
        produk.status_id = status
        produk.kategori_id = kategori
        produk.save()
    return HttpResponseRedirect(reverse('index'))
