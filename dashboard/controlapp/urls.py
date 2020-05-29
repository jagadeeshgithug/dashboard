from django.urls import path
from .views import home,products,customer,orderupdate,deleteorder,productupdate,deleteproduct,createproduct,allorders

urlpatterns = [
    path('',home,name="home"),
    path('products/',products,name="products"),
    path('allorders/',allorders,name="allorders"),
    path('customer/<str:pk>/',customer,name="customer"),
    path('orderupdate/<str:pk>/',orderupdate,name="orderupdate"),
    path('deleteorder/<str:pk>/',deleteorder,name="deleteorder"),
    path('createproduct/',createproduct,name="createproduct"),
    path('productupdate/<str:pk>/',productupdate,name="productupdate"),
    path('deleteproduct/<str:pk>/',deleteproduct,name="deleteproduct"),
]
