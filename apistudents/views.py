from django.shortcuts import render , get_object_or_404
from students.models import Students
from .serializers import Studentserializer , Employeeserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee as employeemodel
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics , viewsets
from blogs.models import Blog , Comments
from blogs.serializers import BlogSerializers , CommentsSerializers
from .Paginations import CustomePagination


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

# class Employee( APIView ):
#     def get( self , request ):
#         employee = employeemodel.objects.all()
#         serilaizer = Employeeserializer( employee , many = True )
#         return Response( serilaizer.data , status=status.HTTP_200_OK )  
#     def put(self , request):
#         serializer = Employeeserializer( data = request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)      
   
# class Employee_PK( APIView ):
#     def get_object( self  , pk ):
#         try:
#             return employeemodel.objects.get( pk = pk )
#         except employeemodel.DoesNotExist:
#             raise Http404
#     def get( self , request , pk ):
#         employee = self.get_object( pk )
#         serializer = Employeeserializer( employee )
#         return Response( serializer.data , status=status.HTTP_200_OK )
#     def put( self , request , pk ):
#         employee = self.get_object( pk )
#         serilazer = Employeeserializer( employee , data = request.data )
#         if serilazer.is_valid():
#             serilazer.save()
#             return Response(serilazer.data , status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete( self , request ,pk ):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response( status=status.HTTP_204_NO_CONTENT )



"""
# mixins 
class Employee(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = employeemodel.objects.all()
    serializer_class = Employeeserializer

    def get(self , request):
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
class Employee_PK(generics.GenericAPIView , mixins.RetrieveModelMixin , mixins.DestroyModelMixin , mixins.UpdateModelMixin ):
    queryset = employeemodel.objects.all()
    serializer_class = Employeeserializer

    def get(self , request , pk):
        return self.retrieve(request,pk)
    
    def put(self , request , pk):
        return self.update(request,pk) 
    
    def delete(self , request , pk):
        return self.destroy(request , pk) 
"""



"""
# Generics singeleAPIView
class Employee(generics.ListAPIView , generics.CreateAPIView):
    queryset = employeemodel.objects.all()
    serializer_class = Employeeserializer


# Generics pk based operations
class Employee_PK(generics.RetrieveAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
    queryset = employeemodel.objects.all()
    serializer_class = Employeeserializer
    lookup_field = 'pk'
"""


#ViewSet
'''
class EmployeeViewset(viewsets.ViewSet):
    def list(self , request):
        queryset = employeemodel.objects.all()
        serializer = Employeeserializer(queryset , many = True)
        return Response(serializer.data)
    
    def create(self , request):
        serializer = Employeeserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self , request , pk=None):
        employee = get_object_or_404(employeemodel , pk = pk)
        serlizer = Employeeserializer(employee)
        return Response(serlizer.data , status=status.HTTP_202_ACCEPTED)
    
    def update(self , request , pk = None):
        employee = get_object_or_404(employeemodel , pk = pk)
        serializer = Employeeserializer(employee , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self , request , pk = None):
        employee = get_object_or_404(employeemodel , pk = pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = employeemodel.objects.all()
    serializer_class = Employeeserializer 
    pagination_class = CustomePagination



#Nested Serializers
class BlogView(generics.ListCreateAPIView):
    queryset =  Blog.objects.all()
    serializer_class = BlogSerializers

class CommentView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers

#PK nested serializers
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'pk'

class CommentsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    lookup_field = 'pk'



