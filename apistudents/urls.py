from django.urls import path
from .views import *

urlpatterns = [ 
    path('students/' , apiStudent),
    path('students/<int:pk>/' , apiStudentPK),
 ]
