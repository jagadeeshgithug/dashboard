from django.urls import path
from .views import home,products,customers

urlpatterns = [
    path('',home,name="home"),
    path('products/',products,name="products"),
    path('customer/',customers,name="customer"),
]
