from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
import requests
from .models import *
from .serializer import *
from django.http import JsonResponse
import subprocess
from rest_framework.decorators import api_view
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo API FINAL'}
        return Response(context)


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

class TipoAulaViewSet(viewsets.ModelViewSet):
    queryset = TipoAula.objects.all()
    serializer_class = TipoAulaSerializer


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class DetalleAccesoViewSet(viewsets.ModelViewSet):
    queryset = DetalleAcceso.objects.all()
    serializer_class = DetalleAccesoSerializer


class AccesoViewSet(viewsets.ModelViewSet):
    queryset = Acceso.objects.all()
    serializer_class = AccesoSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer


@api_view(['GET'])
def get_data(request):
    #http://127.0.0.1:8000/api/mi_vista/?operacion=borrar&id_b=15
    operacion = request.GET.get('operacion', None)
    nombre = request.GET.get('nombre', None)
    valor = request.GET.get('valor', None)
    id_a = request.GET.get('id_a', None)
    id_b = request.GET.get('id_b', None)


    
    datos = []
    if(operacion =="crear"):
        consulta = Mqtt(nombre=nombre, valor=valor)
        consulta.save()
        comando = f"python3 /var/www/html/envia.py '{{'operacion':'crear', 'nombre':'{nombre}', 'valor':'{valor}'}}'"
        ejecutar_comando_terminal(comando)

        
     
        
    if(operacion == "consultar"):
        resultados = Mqtt.objects.all()
        
        for resultado in resultados:
            datos.append({
            'id':resultado.id,
            'nombre': resultado.nombre,
            'valor': resultado.valor,
            'fecha_registro': resultado.fecha_registro
        })
        comando = f"python3 /var/www/html/envia.py '{{'operacion':'consultar'}}'"
        ejecutar_comando_terminal(comando)
    if(operacion =="actualizar"):
        resultado = Mqtt.objects.get(id=id_a)
        resultado.valor = valor
        resultado.save()
        """ comando = f"python3 /var/www/html/envia.py '{{'operacion':'actualizar', 'id':'{id_a}', 'valor':'{valor}'}}'"
        
        ejecutar_comando_terminal(comando) """

        comando = ["python3", "/var/www/html/envia.py "]
        argumento = "{'operacion': 'consulta'}"

        # Ejecuta el comando y obtén la salida
        subprocess.run(comando + [argumento], capture_output=True, text=True)
       
    if(operacion =="borrar"):
        resultado = Mqtt.objects.get(id=id_b)
        resultado.delete()
        comando = f"python3 /var/www/html/envia.py '{{'operacion':'borrar', 'id_b':'{id_b}'}}'"
        ejecutar_comando_terminal(comando)

    return JsonResponse(datos, safe=False)


def ejecutar_comando_terminal(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado.stdout  # Salida del comando ejecutado
        
        # Puedes realizar acciones adicionales con la salida del comando si lo deseas
        
""" class MqttView(APIView):
    
    def get(self,request):
        
        nombre = request.GET.get('nombre')
        valor = request.GET.get('valor')
        dataMqtt= Mqtt(nombre=nombre, valor=valor)
        serMqtt = MqttSerializer(dataMqtt,many=True)
        return Response(serMqtt.data)
    
    def post(self,request):
        serMqtt = MqttSerializer(data=request.data)
        serMqtt.is_valid(raise_exception=True)
        serMqtt.save()
        
        return Response(serMqtt.data)
     """
""" class MqttDetailView(APIView):
    
    def get(self,request,mqtt_id):
        dataMqtt = Mqtt.objects.get(pk=mqtt_id)
        serMqtt = MqttSerializer(dataMqtt)
        return Response(serMqtt.data)
    
    def put(self,request,mqtt_id):
        dataMqtt = Mqtt.objects.get(pk=mqtt_id)
        serMqtt = MqttSerializer(dataMqtt,data=request.data)
        serMqtt.is_valid(raise_exception=True)
        serMqtt.save()
        return Response(serMqtt.data)
    
    def delete(self,request,mqtt_id):
        dataMqtt = Mqtt.objects.get(pk=mqtt_id)
        serMqtt = MqttSerializer(dataMqtt)
        dataMqtt.delete()
        return Response(serMqtt.data) """
