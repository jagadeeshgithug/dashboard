from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

"""this is home page function which is show the all details"""

def home(request):
	orders=Order.objects.all()
	top_orders=Order.objects.order_by('-id')[0:5]
	customers=Customer.objects.all()

	total_orders=orders.count()
	pending=orders.filter(status='Pending').count()
	deliverd=orders.filter(status='Deliverd').count()
	context={
		'orders':top_orders,
		'customers':customers,
		'total_orders':total_orders,
		'pending':pending,
		'deliverd':deliverd
	}
	return render(request, "controlapp/dashboard.html",context)

"""this is product details page"""

def products(request):

	products=Product.objects.all()

	context={
		'products':products
	}
	return render(request, "controlapp/products.html",context)

"""this is customer details page"""

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


def allorders(request):
	orders=Order.objects.all()

	context={
		'orders':orders
	}

	return render(request,"controlapp/orders.html",context)
"""this function is update the status of the orders"""

def orderupdate(request,pk):

	order=Order.objects.get(id=pk)

	form=orderform(instance=order)

	if request.method == 'POST':
		form = orderform(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={
		'form':form
	}

	return render(request,'controlapp/order_form.html',context)



"""this function is delete the order"""

def deleteorder(request,pk):

	order=Order.objects.get(id=pk)

	if request.method=='POST':
		order.delete()
		return redirect('/')

	context={
		'order':order
	}

	return render(request,"controlapp/orderdelete.html",context)

def createproduct(request):

	form=productform()

	if request.method == 'POST':
		form = productform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/products/')

	context={
		'form':form
	}

	return render(request,'controlapp/product_form.html',context)



def productupdate(request,pk):

	product=Product.objects.get(id=pk)

	form=productform(instance=product)

	if request.method == 'POST':
		form = productform(request.POST,instance=product)
		if form.is_valid():
			form.save()
			return redirect('/products/')

	context={
		'form':form
	}

	return render(request,'controlapp/product_form.html',context)

def deleteproduct(request,pk):

	product=Product.objects.get(id=pk)

	if request.method=='POST':
		product.delete()
		return redirect('/products/')

	context={
		'product':product
	}

	return render(request,"controlapp/productdelete.html",context)
