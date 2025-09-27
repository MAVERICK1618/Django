from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
from apistudents import views


router = DefaultRouter()
router.register("employees" , views.EmployeeViewset , basename="employee")

urlpatterns = [ 
    path('students/' , apiStudent),
    path('students/<int:pk>/' , apiStudentPK),


    # path('employee/' , Employee.as_view()),
    # path('employee/<int:pk>/' , Employee_PK.as_view())
    
    path('' , include(router.urls))

 ]
