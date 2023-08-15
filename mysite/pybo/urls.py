from django.urls import path 

from . import views 

# app의 url 관리 
urlpatterns = [ 
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),

]