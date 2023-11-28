from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Status, Produk
from django.urls import reverse
from .forms import ProdukForm
from django.contrib import messages

def index(request):
    status = Status.objects.get(nama_status = "bisa dijual")
    context = {
        'statuss' : status
    }
    return render(request, 'toko/index.html', context)

def add_produk(request):
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
    return HttpResponseRedirect(reverse('index'))

def edit_produk(request, produk_id): 
    instance = get_object_or_404(Produk, id=produk_id)
    form = ProdukForm(request.POST or None, instance=instance)
    if form.is_valid():
        produk = form.save(commit=False)
        produk.save()
        messages.success(request, "Data updated.")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'toko/form.html', {'form': form}) 
 
