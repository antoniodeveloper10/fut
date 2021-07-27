from django.db import models

# Create your models here.
class quadras(models.Model):
    id_quadra= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    Tipo = (
        ('s', 'Salão'),
        ('c', 'Campo'),
        ('a', 'Areia'),
        ('soc', 'Society'),
    )
    tipo_quadra = models.CharField(max_length=3,choices=Tipo,blank=False,null=False,default='s')  
    contato =  models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'quadras'
        verbose_name = 'quadra'
        verbose_name_plural = 'quadras'