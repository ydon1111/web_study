from re import template
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from django.db import connection

from . import models

from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd 
import numpy as np 

# Create your views here.

def index(request):

    heatRatePlot = models.heartRate()


    # return HttpResponse('하이 !!! 호랑이')
    return render(request,"index.html",context={'plot_div':heatRatePlot['plot_div'],'danger':heatRatePlot['danger']})