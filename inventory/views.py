
from api.views import ListInventories, InventoryDetails
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class viewInventories(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory-list.html'

    def get(self, request):

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
