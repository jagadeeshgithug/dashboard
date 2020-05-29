
from django.forms import ModelForm

from .models import Order,Product


class orderform(ModelForm):

	class Meta:
		model= Order
		fields= '__all__'


class productform(ModelForm):

	class Meta:
		model= Product
		fields= '__all__'
