from django.db import models

# Create your models here.
class jogadores(models.Model):
    id_jogador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nasc = models.DateTimeField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True,default=0)
    jogos_realizados = models.IntegerField(blank=True, null=True,default=0)
    jogos_furados = models.IntegerField(blank=True, null=True,default=0)
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sexo_jogador = models.CharField(max_length=1,choices=SEXO,blank=False,null=False,default='M')  
    contato =  models.CharField(max_length=50, blank=True, null=True)
    TIPO = (
        ('L', 'Linha'),
        ('G', 'Goleiro')
    )
    tipo_jogador = models.CharField(max_length=1,choices=TIPO,blank=False,null=False,default='L')
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'jogadores'
        verbose_name = 'jogador'
        verbose_name_plural = 'jogadores'
