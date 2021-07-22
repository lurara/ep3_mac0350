from django.urls import path

from . import views

urlpatterns = [
    path('agregacao', views.agregacao, name='agregacao'), #http://localhost:8000/ep3/agregacao
    path('query1', views.query1, name='query1'), #http://localhost:8000/ep3/query1
    path('query2', views.query2, name='query2'), #http://localhost:8000/ep3/query2
    path('', views.index, name='index')
]
