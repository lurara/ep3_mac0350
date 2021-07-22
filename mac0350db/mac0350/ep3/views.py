#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
#from .models import Usuario
#from .models import Perfil
from django.db import connection
from collections import namedtuple
from django.template import loader

def index(request):
    return HttpResponse("MAC0350: EP3")

def query1(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_usuario')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query1.html')
    context = {'query1_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query2(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT u.nome, u.login, u.cpf, string_agg(p.tipo, \', \') as perfis FROM ep3_usuario as u\
                LEFT JOIN ep3_usuario_possui_perfil as possui\
                ON u.id = possui.usuario_id\
                JOIN ep3_perfil as p\
                ON possui.perfil_id = p.id\
                GROUP BY u.nome, u.login, u.cpf\
                ')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('query2.html')
    context = {'query2_result_list': result,}
    
    return HttpResponse(template.render(context, request))
#metodos auxiliares
def agregacao(request): # arrumar agregacao
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT ag.data_de_realizacao, ag.data_de_solicitacao, \
                p.nome as paciente , am.codigo_amostra as amostra, e.virus as exame\
                FROM ep3_agregado_paciente_exame_amostra as ag\
                JOIN ep3_paciente as p\
                ON ag.paciente_id = p.id\
                JOIN ep3_amostra as am\
                ON ag.amostra_id = am.id\
                JOIN ep3_exame as e\
                ON ag.exame_id = e.id\
                ')
        """cursor.execute('\
                SELECT  * FROM ep3_agregado_paciente_exame_amostra')"""
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('agregacao.html')
    context = {'agregacao_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result
