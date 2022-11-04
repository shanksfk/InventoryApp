
from django.urls import path
from .views import viewInventories, viewInventoryDetails
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('inventory', ViewInventory)
# urlpatterns = router.urls


urlpatterns = [


    path('inventories', viewInventories.as_view(), name='inventory-list'),
    path('inventory/<str:pk>', viewInventoryDetails.as_view(),
         name='inventory-details'),
]
