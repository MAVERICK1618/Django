from django.urls import path
from .views import *

urlpatterns = [ 
    path('students/' , apiStudent),
    path('students/<int:pk>/' , apiStudentPK),


    path('employee/' , Employee.as_view()),
    path('employee/<int:pk>/' , Employee_PK.as_view())
 ]
