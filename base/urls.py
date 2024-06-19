from django.urls import path
from .views import login,register,CategoryApiView, ProductApiView, OrderApiView,WarehouseApiView,ShipmentApiView,CustomerApiView,SupplierApiView
urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('category/',CategoryApiView.as_view({'get':'list','post':'create'}),name='category'),
    path('category/<int:pk>',CategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='category_details'),
    path('product/',ProductApiView.as_view({'get':'list','post':'create'}),name='product'),
    path('product/<int:pk>',ProductApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='product_details'),
    path('supplier/',SupplierApiView.as_view({'get':'list','post':'create'}),name='supplier'),
    path('supplier/<int:pk>',SupplierApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='supplier_details'),
    path('order/',OrderApiView.as_view({'get':'list','post':'create'}),name='order'),
    path('order/<int:pk>',OrderApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='order_details'),
    path('customer/',CustomerApiView.as_view({'get':'list','post':'create'}),name='customer'),
    path('customer/<int:pk>',CustomerApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='customer_details'),
    path('warehouse/',WarehouseApiView.as_view({'get':'list','post':'create'}),name='warehouse'),
    path('warehouse/<int:pk>',WarehouseApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='warehouse_details'),
    path('shipment/',ShipmentApiView.as_view({'get':'list','post':'create'}),name='shipment'),
    path('shipment/<int:pk>',ShipmentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='shipment_details'),
]