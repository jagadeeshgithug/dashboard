from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,Group 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *
from .decorators import unauthenticate_user,allowed_users,admin_only
# Create your views here.

"""this is home page function which is show the all details"""
@unauthenticate_user
def registerpage(request):
	form=usercreationform()

	if request.method == 'POST':
		form=usercreationform(request.POST)
		if form.is_valid():
			user=form.save()
			group=Group.objects.get(name='customers')
			user.groups.add(group)
			username=form.cleaned_data.get('username')
			messages.success(request,"Account succesfully create for "+ username)
			return redirect('/login/')

	context={
		'form':form
	}
	return render(request,"controlapp/register.html",context)
@unauthenticate_user
def loginpage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,"Username OR Password is incorrect")
	return render(request,'controlapp/login.html')

def logoutpage(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
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
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])	
def products(request):

	products=Product.objects.all()

	myfilter=productfilter(request.GET,queryset=products)
	products=myfilter.qs
	context={
		'products':products,
		'myfilter':myfilter
	}
	return render(request, "controlapp/products.html",context)

"""this is customer details page"""
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])	
def customer(request,pk):
	customer=Customer.objects.get(id=pk)

	orders=customer.order_set.all()
	total_orders=orders.count()

	myfilter=orderfilter(request.GET,queryset=orders)
	orders=myfilter.qs
	context={
		'customer':customer,
		'orders':orders,
		'total_orders':total_orders,
		'myfilter':myfilter
	}
	return render(request, "controlapp/customers.html",context)

@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
def allorders(request):
	orders=Order.objects.all()

	myfilter=orderfilter(request.GET,queryset=orders)
	orders=myfilter.qs

	context={
		'orders':orders,
		'myfilter':myfilter
	}

	return render(request,"controlapp/orders.html",context)


"""this function is update the status of the orders"""
@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
def deleteorder(request,pk):

	order=Order.objects.get(id=pk)

	if request.method=='POST':
		order.delete()
		return redirect('/')

	context={
		'order':order
	}

	return render(request,"controlapp/orderdelete.html",context)


@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
def deleteproduct(request,pk):
	product=Product.objects.get(id=pk)

	if request.method=='POST':
		product.delete()
		return redirect('/products/')

	context={
		'product':product
	}
	return render(request,"controlapp/productdelete.html",context)


@login_required(login_url='login')
def userpage(request):
	return render(request,"controlapp/userpage.html")