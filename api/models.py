from django.db import models

class Acceso(models.Model):
    nombreAula = models.CharField(max_length=200)
    nombreProfesor = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    pub_date = models.DateTimeField('fecha de registro',auto_now=True)

