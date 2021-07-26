#from django.db import models

# Create your models here.

from django.db import models


class Perfil(models.Model):
    codigo = models.CharField(max_length=255) # não há necessidade de chave privada
    tipo = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.codigo +','+ self.tipo
    
class Usuario(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    area_de_pesquisa = models.CharField(max_length=255, blank=True, null=True)
    instituicao = models.CharField(max_length=255, blank=True, null=True)
    data_de_nascimento = models.DateField('data de nascimento')
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    perfis = models.ManyToManyField(Perfil, through='Usuario_Possui_Perfil')
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['login'], name='unique_login')
                ]

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    cpf = models.CharField(max_length=11) 
    nome = models.CharField(max_length=255) 
    endereco = models.CharField(max_length=255) 
    nascimento = models.DateField('data de nascimento')
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['cpf'], name='unique_paciente')
                ]
    
    def __str__(self):
        return self.nome
        
class Exame(models.Model):
    tipo = models.CharField(max_length=255) 
    virus = models.CharField(max_length=255)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, default='')
    #paciente = models.ManyToManyField(Paciente, through='Agregado_Paciente_Exame_Amostra') # se eu usar esse consigo filtrar
    # relação 1:n de paciente para exame

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['tipo', 'virus'], name='unique_exame')
                ]
        
    def __str__(self):
        return self.virus +','+ self.tipo
        
class Amostra(models.Model):
    codigo_amostra = models.CharField(max_length=255) 
    metodo_de_coleta = models.CharField(max_length=255) 
    material = models.CharField(max_length=255)
    #exame = models.ManyToManyField(Exame, through='Agregado_Paciente_Exame_Amostra')
    # uma amostra resulta de um exame de um paciente

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['codigo_amostra'], name='unique_amostra')
                ]
        
    def __str__(self):
        return self.codigo_amostra

#relacionamento Possui
class Usuario_Possui_Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['usuario', 'perfil'], name='unique_usuario_perfil')
                ]

class Agregado_Paciente_Exame_Amostra(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT) # um paciente pode ter mais de uma agregação
    exame = models.OneToOneField(Exame, on_delete=models.PROTECT)
    amostra = models.ForeignKey(Amostra, on_delete=models.PROTECT)
    data_de_realizacao = models.DateTimeField(auto_now_add=True)
    data_de_solicitacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['paciente', 'exame', 'amostra','data_de_realizacao'],
                name='unique_agregado') ]

    def __str__(self):
        return self.paciente.nome +','+ self.exame.virus +','+ self.exame.tipo +','+ self.amostra.codigo_amostra