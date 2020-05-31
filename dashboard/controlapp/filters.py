
import django_filters
from django_filters import DateFilter
from .models import *


class orderfilter(django_filters.FilterSet):
	start_date=DateFilter(field_name='date_created',lookup_expr='gte')
	end_date=DateFilter(field_name='date_created',lookup_expr='lte')
	class Meta:
		model=Order 
		fields='__all__'
		exclude=['date_created']

class productfilter(django_filters.FilterSet):
	start_date=DateFilter(field_name='date_created',lookup_expr='gte')
	end_date=DateFilter(field_name='date_created',lookup_expr='lte')
	
	class Meta:
		model=Product 
		fields='__all__'
		exclude=['date_created','discription','tags']