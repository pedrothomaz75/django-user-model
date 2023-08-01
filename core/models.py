from django.db import models

# Import do get_user_model
from django.contrib.auth import get_user_model

class Post(models.Model):
    # get_user_model = retorna um módulo do usuário
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título',  max_length=100)
    texto = models.TextField('Texto', max_length=400)

    # Função de retorno na ORM do django
    def __str__(self):
        return self.titulo