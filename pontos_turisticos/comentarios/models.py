from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True) # automatico
    aprovado = models.BooleanField(default=True) # automatico

    def __str__(self):
        return self.usuario.username
