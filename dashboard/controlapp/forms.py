
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order,Product,Customer


class orderform(ModelForm):

	class Meta:
		model= Order
		fields= '__all__'


class productform(ModelForm):

	class Meta:
		model= Product
		fields= '__all__'


class usercreationform(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']

class customerdetialform(ModelForm):
	class Meta:
		model=Customer
		fields=['name','phone','email','profile_pic']