#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuario, Perfil, Usuario_Possui_Perfil, Paciente, Amostra, Exame,Agregado_Paciente_Exame_Amostra

class PerfilInline(admin.TabularInline):
    model = Usuario_Possui_Perfil
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PerfilInline,)

class Agregado(admin.TabularInline):
    model = Agregado_Paciente_Exame_Amostra
    extra = 1

class ResultaExame(admin.ModelAdmin):
    inlines = (Agregado,)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Perfil)
admin.site.register(Paciente)
admin.site.register(Amostra)
admin.site.register(Exame, ResultaExame)
admin.site.register(Agregado_Paciente_Exame_Amostra)
#como ligar os trÊs?

