from django.contrib import admin
from jogadores.models import jogadores

# Register your models here.

# Register your models here.
@admin.register(jogadores)
class jogadorAdmin(admin.ModelAdmin):
    list_display = [
        'id_jogador', 
        'nome',
        'data_nasc',
        'nivel',
        'jogos_realizados',
        'jogos_furados',
        'sexo_jogador',
        'contato',
        'tipo_jogador',
        'ativo',
        'data_cadastro' 
    ]

    # tranformar um campo sรณ leitura
    readonly_fields = ('jogos_realizados','jogos_furados',)
    # ordena pelo campo nome
    ordering = ('nome',)
    # informa quais campos vao receber links
    list_display_links = ('nome', 'data_nasc')
    # campo de busca
    search_fields = ('nome',)


    
