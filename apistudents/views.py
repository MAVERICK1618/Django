from django.shortcuts import render
from students.models import Students
from .serializers import Studentserializer , Employeeserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee as employeemodel
from django.http import Http404

# Create your views here.

@api_view(['GET' , 'POST'])
def apiStudent(request):
    if request.method == 'GET':
        student = Students.objects.all()
        serializers = Studentserializer( student , many = True )
        return Response( serializers.data , status= status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = Studentserializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT' , 'DELETE'])
def apiStudentPK(request , pk):
    try:
        student = Students.objects.get(pk = pk)   #get is used for take particular object
    except Students.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Studentserializer(student)
        return Response( serializer.data , status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Studentserializer( student , data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
 

#  creating Class Based Views

class Employee( APIView ):
    def get( self , request ):
        employee = employeemodel.objects.all()
        serilaizer = Employeeserializer( employee , many = True )
        return Response( serilaizer.data , status=status.HTTP_200_OK )  
    def put(self , request):
        serializer = Employeeserializer( data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)      
   
class Employee_PK( APIView ):
    def get_object( self  , pk ):
        try:
            return employeemodel.objects.get( pk = pk )
        except employeemodel.DoesNotExist:
            raise Http404
    def get( self , request , pk ):
        employee = self.get_object( pk )
        serializer = Employeeserializer( employee )
        return Response( serializer.data , status=status.HTTP_200_OK )
    def put( self , request , pk ):
        employee = self.get_object( pk )
        serilazer = Employeeserializer( employee , data = request.data )
        if serilazer.is_valid():
            serilazer.save()
            return Response(serilazer.data , status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete( self , request ,pk ):
        employee = self.get_object(pk)
        employee.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )