from re import template
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render


from django.db import connection


# Create your views here.

def index(request):
    print('index call',type(request),request)
    # return HttpResponse('하이 !!! 호랑이')
    return render(request,"index.html")

def tiger(request):
    print('tiger : ',type(request),request)
    
    # context = {
    #     'name' : '홍길동',
    #     'age' : '20',
    #     'salary' : '500',
    # }

    data = [
        '호랑이',
        '코끼리',
        '독수리'
    ]
    context = {
        'data' : data
    }

    return render(request,"tiger.html",context)

def lion(request):
    return render(request,"lion.html")


def monkey(request,testId):

    try:
        cursor = connection.cursor()
        print("@@@@@@@", cursor)    

        strSql = "select * from table02;"
        result = cursor.execute(strSql)
        books = cursor.fetchall()

        print("db_data",result)
        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("connection fail")



    return render(request,"monkey.html")


def eagle(request):
    name = request.POST['name']
    age = int(request.POST['age'])
    salary = int(request.POST['salary'])

    try:
        cursor = connection.cursor()
        strSql = "insert into db01.table02(name,age,salary) values ('%s',%d,%d);" %(name,age,salary)
        result = cursor.execute(strSql)
        # books = cursor.fetchall()

        print("db_data",result)
        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("connection fail")
    


    return render(request,"eagle.html")


