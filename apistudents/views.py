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
    
   