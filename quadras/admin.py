from django.contrib import admin
from quadras.models import quadras

# Register your models here.

# Register your models here.
@admin.register(quadras)
class quadrasAdmin(admin.ModelAdmin):
    list_display = [
        'id_quadra', 
        'nome',
        'tipo_quadra',
        'contato',
        'ativo',
        'data_cadastro' 
    ]

    # tranformar um campo sรณ leitura
    readonly_fields = ('data_cadastro','id_quadra',)
    # ordena pelo campo nome
    ordering = ('nome',)
    # informa quais campos vao receber links
    list_display_links = ('nome', 'id_quadra')
    # campo de busca
    search_fields = ('nome',)



