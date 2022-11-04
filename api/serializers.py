from rest_framework import serializers
from .models import Inventory, Supplier


class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class InventorySerializers(serializers.ModelSerializer):
    supplier = SupplierSerializers()

    class Meta:
        model = Inventory
        fields = '__all__'
