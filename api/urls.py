
from django.urls import path, include, re_path
from .views import InventoryDetails, getRoutes, ListInventories
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('inventory', ViewInventory)
# urlpatterns = router.urls


urlpatterns = [

    path('', getRoutes, name='api-routes'),
    path('inventory/', ListInventories.as_view(), name='api-inventory'),
    re_path('^inventory/(?P<name>.+)/$', ListInventories.as_view()),
    path('inventory/<str:pk>', InventoryDetails.as_view(),
         name='api-inventory-details'),
]
