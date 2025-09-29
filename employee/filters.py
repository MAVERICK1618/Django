
import django_filters
from .models import Employee

class EmployeeFilter( django_filters.FilterSet ):
    emp_role = django_filters.CharFilter(field_name='emp_role' , lookup_expr='iexact')
    id_max = django_filters.CharFilter(method='filter_by_id_range')
    id_min = django_filters.CharFilter(method='filter_by_id_range')

    class Meta:
        model = Employee
        fields = ['emp_role' , 'id_max' , 'id_min']
    
    def filter_by_id_range(self , queryset , name , value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte = value)
        return queryset

    