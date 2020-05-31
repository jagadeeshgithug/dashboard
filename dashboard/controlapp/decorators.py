from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticate_user(view_fun):

	def wrapper_fun(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_fun(request,*args,*kwargs)

	return wrapper_fun

def allowed_users(allowed_roles=[]):
	def decorators(view_fun):
		def wrapper_fun(request,*args,**kwargs):
			group=None
			if request.user.groups.exists():
				group=request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_fun(request,*args,**kwargs)
			else:
				return HttpResponse("you are not autherized person to this page")

		return wrapper_fun
	return decorators

def admin_only(view_fun):
	def wrapper_fun(request,*args,**kwargs):
		group=None
		if request.user.groups.exists():
			group=request.user.groups.all()[0].name
		if group == 'customers':
			return redirect('userpage')
		if group == 'admin':
			return view_fun(request,*args,**kwargs)
	return wrapper_fun