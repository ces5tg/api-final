from .models import *
from rest_framework import serializers

class AccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceso
        fields = ('id', 'nombreAula', 'nombreProfesor','password', 'pub_date')


