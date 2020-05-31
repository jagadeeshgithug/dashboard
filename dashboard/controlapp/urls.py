from django.urls import path
from .views import *

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
    path('userpage/',userpage,name='userpage'),

    path('register/',registerpage,name='register'),
    path('login/',loginpage,name='login'),
    path('logout/',logoutpage,name='logout'),

]
