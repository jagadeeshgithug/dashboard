from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
	orders=Order.objects.all()
	customers=Customer.objects.all()

	total_orders=orders.count()
	pending=orders.filter(status='Pending').count()
	deliverd=orders.filter(status='Deliverd').count()
	context={
		'orders':orders,
		'customers':customers,
		'total_orders':total_orders,
		'pending':pending,
		'deliverd':deliverd
	}
	return render(request, "controlapp/dashboard.html",context)

def products(request):

	products=Product.objects.all()

	context={
		'products':products
	}
	return render(request, "controlapp/products.html",context)

def customer(request,pk):
	customer=Customer.objects.get(id=pk)

	orders=customer.order_set.all()
	total_orders=orders.count()
	context={
		'customer':customer,
		'orders':orders,
		'total_orders':total_orders
	}
	return render(request, "controlapp/customers.html",context)