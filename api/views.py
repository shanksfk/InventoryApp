from django_filters.rest_framework import FilterSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inventory, Supplier
from .serializers import InventorySerializers, SupplierSerializers
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from django_filters import rest_framework as dffilters


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/inventory',
        'GET /api/inventory/:id'
    ]
    return Response(routes)


class InventoryFilter(dffilters.FilterSet):
    class Meta:
        model = Inventory
        fields = ['name']


class ListInventories(generics.ListAPIView, FilterSet):

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def consume_data(self, request):

        inventories = Inventory.objects.all()
        serializer = InventorySerializers(inventories, many=True)
        return Response({'inventories': serializer.data})


class InventoryDetails(APIView):
    def get(self, request, pk):
        inventories = Inventory.objects.get(id=pk)
        serializer = InventorySerializers(inventories)
        return Response({'inventory': serializer.data})
