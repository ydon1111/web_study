from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import TestResult1HHumi
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def blog(request):
    
    resultlast = TestResult1HHumi.objects.last()
    resultlist = TestResult1HHumi.objects.all()
    print("@@saaaa@@",TestResult1HHumi.objects.last())
    return render(request,'main/blog.html', {"resultlast":resultlast ,"resultlist":resultlist})







# def blog(request):
    
#     resultlist = TestResult1HHumi.objects.values()
#     # print("@@saaaa@@", resultlist)
#     context = {'resultlist':resultlist}

#     print("@@@@@",context)
#     return HttpResponse(context)
