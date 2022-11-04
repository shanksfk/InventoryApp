
from api.views import ListInventories, InventoryDetails
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from api.models import Inventory, Supplier
from api.serializers import InventorySerializers, SupplierSerializers
from django_filters import rest_framework as filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class viewInventories(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory-list.html'
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get(self, request):
        # inventories = Inventory.objects.all()
        # serializer = InventorySerializers(inventories, many=True)
        # # print(serializer.data)
        # return Response({'inventories': serializer.data})
        return ListInventories.consume_data(self, request)


class viewInventoryDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory-detail.html'

    def get(self, request, pk):
        # inventories = Inventory.objects.all()
        # serializer = InventorySerializers(inventories, many=True)
        # # print(serializer.data)
        # return Response({'inventories': serializer.data})
        return InventoryDetails.get(self, request, pk)
