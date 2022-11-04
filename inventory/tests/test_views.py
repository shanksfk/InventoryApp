from django.test import TestCase, Client
from django.urls import reverse

from api.models import Inventory


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('inventory-list')
        self.detail_url = reverse('inventory-details', args=['1'])
        self.api_inventory = reverse('api-inventory')
        self.inv1 = Inventory.objects.create(
            name='Painkiller', description='hellotext', note='here', stock=9, availability=True)

    def test_list_inventory_GET(self):

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory-list.html')
        # self.detail_url = reverse('inventory-detail', args=['1'])

    def test_detail_inventory_GET(self):

        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory-detail.html')
        # self.detail_url = reverse('inventory-detail', args=['1'])

    def test_api_inventory_GET(self):

        response = self.client.get(self.api_inventory)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response)
        # self.detail_url = reverse('inventory-detail', args=['1'])
