from django.shortcuts import render

# Create your views here.

def if_condition(request):
    d={'a':100,'b':80}
    return render (request,'if_condition.html',d)

def if_else_condition(request):
    d={'a':10,'b':20}
    return render (request,'if_else_condition.html',d)

def if_elif_else_condition(request):
    d={'a':10,'b':20,'c':30}
    return render (request,'if_elif_else_condition.html',d)

def nested_if_condition(request):
    d={'a':100,'b':80,'c':35}
    return render (request,'nested_if_condition.html',d)