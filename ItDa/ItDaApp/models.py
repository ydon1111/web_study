from django.db import models


from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd 
import numpy as np 
# Create your models here.


def heartRate():
    file_path = '/Users/yeongdon/Desktop/workspace/정밀의료해커톤/ItDa/ItDaApp/data/한국건강증진개발원_보건소 모바일 헬스케어_심박수_20220101.csv'
    df = pd.read_csv(file_path,encoding='cp949')
    df = df.drop(['최고심박','최저심박','심박수_배열'], axis=1)

    df.head()
    df.columns = ['date','bpm']
    df.date = pd.to_datetime(df.date)
    df.bpm = pd.to_numeric(df.bpm)

    df = df.replace(0, np.NaN)
    df = df.dropna(axis=0)
    
    x = df['date']
    y = df['bpm']

    dx =[]
    i = 0
    for idx,data in enumerate(df['bpm']):
        if data > 180:
            i += 1 
            dx.append(str(i)+"번 =" +str(df.iloc[idx]['date'])+" 심박수 : "+str(df.iloc[idx]['bpm']))
        elif data < 10:
            i += 1
            dx.append(str(i)+"번 = " +str(df.iloc[idx]['date'])+" 심박수 : "+str(df.iloc[idx]['bpm']))
        
   
   

    graphs = []




    graphs.append(
    go.Scatter(x=x, y=y, mode='lines', name='HeartRate'))
        

    layout = {
        'title': 'HeartRate',
        'xaxis_title': 'Date',
        'yaxis_title': 'BPM',
        'height': 420,
        'width': 560,
    }

        # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')


    return {"plot_div":plot_div,"danger":dx}