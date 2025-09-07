from django.shortcuts import render
from django.http import HttpResponse

def students(request):

    student = [{
        "id" : 1 ,
        "name" : "ArunKumar" , 
        "role" : "Software Developer" ,
        "Hobbies" : [ 'Problem Solving ' , "Self Care" , 'Reading Books' ],
    }]

    return HttpResponse(student)
