from django.urls import path

from . import views

urlpatterns = [
    path('agregacao', views.agregacao, name='agregacao'), #http://localhost:8000/ep3/agregacao
    path('query_usuario', views.query_usuario, name='query_usuario'), #http://localhost:8000/ep3/query1
    path('query_usuario_perfil', views.query_usuario_perfil, name='query_usuario_perfil'), #http://localhost:8000/ep3/query2
    path('query_perfis', views.query_perfis, name='query_perfis'),
    path('query_pacientes', views.query_pacientes, name='query_pacientes'),
    path('query_exames', views.query_exames, name='query_exames'),
    path('query_amostras', views.query_amostras, name='query_amostras'),
    path('', views.index, name='index')
]
