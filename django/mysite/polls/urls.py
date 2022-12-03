from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('tiger/', views.tiger, name='tiger'),
    # path('lion/',views.lion, name='lion'),
    
]
