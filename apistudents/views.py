from django.shortcuts import render
from students.models import Students
from .serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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

@api_view(['GET' , 'PUT'])
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
        

    
   