from typing import Any
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')

    # Exclue o drop down de escolha de usuário
    exclude = ['autor',]

    # Função que muda o nome de apresentação do autor na ORM, de nome do usuário para nome completo
    def _autor(self, instace):
        return f'{instace.autor.get_full_name()}'
    
    # Função que consulta o banco de dados
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    
    # Função que diz que quem tá salvado algo no post é a própria pessoa que está logada 
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request ,obj, form, change)