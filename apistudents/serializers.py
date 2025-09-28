from rest_framework import serializers
from students.models import *
from employee.models import Employee
from blogs.models import Blog , Comments


class Studentserializer( serializers.ModelSerializer ):
    class Meta:
        model = Students
        fields = "__all__"
    
class Employeeserializer( serializers.ModelSerializer ):
    class Meta:
        model = Employee
        fields = "__all__"


