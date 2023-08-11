from django.shortcuts import render
from .models import Question

# # Create your views here.

# from django.http import HttpResponse

def index(requset):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(requset, 'pybo/question_list.html',context)
