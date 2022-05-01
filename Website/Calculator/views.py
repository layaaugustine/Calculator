import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def operation(request):
    val1 = int(request.POST['num1'])
    val2= int(request.POST['num2'])
    sign=request.POST['op']
    if sign=='+':
        val=val1+val2
    elif sign=='-':
        val=val1-val2
    elif sign=='/':
        val=val1/val2
    elif sign=='*':
        val=val1*val2
    else:
        return HttpResponse("Invalid Operator")
    return render(request,'result.html',{'Result':val})