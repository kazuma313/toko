from rest_framework import serializers
from toko.models import Produk
  
class TokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = "__all__"
        