from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

class AccesosView(APIView):
    
    def get(self,request):
        dataAcceso = Acceso.objects.all()
        serAccesos = AccesoSerializer(dataAcceso,many=True)
        return Response(serAccesos.data)
    
    def post(self,request):
        serAcceso = AccesoSerializer(data=request.data)
        serAcceso.is_valid(raise_exception=True)
        serAcceso.save()
        
        return Response(serAcceso.data)
    
class AccesoDetailView(APIView):
    
    def get(self,request,acceso_id):
        dataAcceso = Acceso.objects.get(pk=acceso_id)
        serAcceso = AccesoSerializer(dataAcceso)
        return Response(serAcceso.data)
    
    def put(self,request,acceso_id):
        dataAcceso = Acceso.objects.get(pk=acceso_id)
        serAcceso = AccesoSerializer(dataAcceso,data=request.data)
        serAcceso.is_valid(raise_exception=True)
        serAcceso.save()
        return Response(serAcceso.data)
    
    def delete(self,request,acceso_id):
        dataAcceso = Acceso.objects.get(pk=acceso_id)
        serAcceso = AccesoSerializer(dataAcceso)
        dataAcceso.delete()
        return Response(serAcceso.data)