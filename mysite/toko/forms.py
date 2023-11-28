from django import forms  
from .models import Produk
  
class ProdukForm(forms.ModelForm):  
    class Meta:  
        model = Produk  
        fields = "__all__"  
        
        # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(ProdukForm, self).clean()
         
        # extract the username and text field from the data
        nama_produk = self.cleaned_data.get('nama_produk')
        harga = self.cleaned_data.get('harga')
 
        # conditions to be met for the username length
        if len(nama_produk) < 10:
            self._errors['nama_produk'] = self.error_class([
                'Minimum 5 characters required'])
        if harga < 1000:
            self._errors['harga'] = self.error_class([
                'Harga minimum of 1000'])
 
        # return any errors if found
        return self.cleaned_data