
import django_filters

from .models import *


class orderfilter(django_filters.FilterSet):
	class Meta:
		model=Order 
		fields='__all__'
		exclude=['date_created']

class productfilter(django_filters.FilterSet):
	class Meta:
		model=Product 
		fields='__all__'
		exclude=['date_created','discription','tags']