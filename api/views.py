from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo API FINAL'}
        return Response(context)

class ZonaView(APIView):
    
    def get(self,request):
        dataZona = Zona.objects.all()
        serZona = ZonaSerializer(dataZona,many=True)
        return Response(serZona.data)
    
    def post(self,request):
        serZona = ZonaSerializer(data=request.data)
        serZona.is_valid(raise_exception=True)
        serZona.save()
        
        return Response(serZona.data)
    
class ZonaDetailView(APIView):
    
    def get(self,request,zona_id):
        dataZona = Zona.objects.get(pk=zona_id)
        serZona = ZonaSerializer(dataZona)
        return Response(serZona.data)
    
    def put(self,request,zona_id):
        dataZona = Zona.objects.get(pk=zona_id)
        serZona = ZonaSerializer(dataZona,data=request.data)
        serZona.is_valid(raise_exception=True)
        serZona.save()
        return Response(serZona.data)
    
    def delete(self,request,zona_id):
        dataZona = Zona.objects.get(pk=zona_id)
        serZona = ZonaSerializer(dataZona)
        dataZona.delete()
        return Response(serZona.data)
    
    #============================================================================

class TipoAulaView(APIView):
    
    def get(self,request):
        dataTipoAula = TipoAula.objects.all()
        serTipoAula = TipoAulaSerializer(dataTipoAula,many=True)
        return Response(serTipoAula.data)
    
    def post(self,request):
        serTipoAula = TipoAulaSerializer(data=request.data)
        serTipoAula.is_valid(raise_exception=True)
        serTipoAula.save()
        
        return Response(serTipoAula.data)
    
class TipoAulaDetailView(APIView):
    
    def get(self,request,tipo_aula_id):
        dataTipoAula = TipoAula.objects.get(pk=tipo_aula_id)
        serTipoAula = TipoAulaSerializer(dataTipoAula)
        return Response(serTipoAula.data)
    
    def put(self,request,tipo_aula_id):
        dataTipoAula = TipoAula.objects.get(pk=tipo_aula_id)
        serTipoAula = TipoAulaSerializer(dataTipoAula,data=request.data)
        serTipoAula.is_valid(raise_exception=True)
        serTipoAula.save()
        return Response(serTipoAula.data)
    
    def delete(self,request,tipo_aula_id):
        dataTipoAula = TipoAula.objects.get(pk=tipo_aula_id)
        serTipoAula = TipoAulaSerializer(dataTipoAula)
        dataTipoAula.delete()
        return Response(serTipoAula.data)
    
    #============================================================================

class AulaView(APIView):
    
    def get(self,request):
        dataAula = Aula.objects.all()
        serAula = AulaSerializer(dataAula,many=True)
      
        return Response(serAula.data)
    
    def post(self,request):
        serAula = AulaSerializer(data=request.data)
        serAula.is_valid(raise_exception=True)
        serAula.save()
        
        return Response(serAula.data)
    
class AulaDetailView(APIView):
    
    def get(self,request,aula_id):
        dataAula = Aula.objects.get(pk=aula_id)
        serAula = AulaSerializer(dataAula)
        return Response(serAula.data)
    
    def put(self,request,aula_id):
        dataAula = Aula.objects.get(pk=aula_id)
        serAula = AulaSerializer(dataAula,data=request.data)
        serAula.is_valid(raise_exception=True)
        serAula.save()
        return Response(serAula.data)
    
    def delete(self,request,aula_id):
        dataAula = Aula.objects.get(pk=aula_id)
        serAula = AulaSerializer(dataAula)
        dataAula.delete()
        return Response(serAula.data)
    
    #============================================================================

class DispositivoView(APIView):
    
    def get(self,request):
        dataDispositivo = Dispositivo.objects.all()
        serDispositivo = DispositivoSerializer(dataDispositivo,many=True)
        return Response(serDispositivo.data)
    
    def post(self,request):
        serDispositivo = DispositivoSerializer(data=request.data)
        serDispositivo.is_valid(raise_exception=True)
        serDispositivo.save()
        
        return Response(serDispositivo.data)
    
class DispositivoDetailView(APIView):
    
    def get(self,request,dispositivo_id):
        dataDispositivo = Dispositivo.objects.get(pk=dispositivo_id)
        serDispositivo = DispositivoSerializer(dataDispositivo)
        return Response(serDispositivo.data)
    
    def put(self,request,dispositivo_id):
        dataDispositivo = Dispositivo.objects.get(pk=dispositivo_id)
        serDispositivo = DispositivoSerializer(dataDispositivo,data=request.data)
        serDispositivo.is_valid(raise_exception=True)
        serDispositivo.save()
        return Response(serDispositivo.data)
    
    def delete(self,request,dispositivo_id):
        dataDispositivo = Dispositivo.objects.get(pk=dispositivo_id)
        serDispositivo = DispositivoSerializer(dataDispositivo)
        dataDispositivo.delete()
        return Response(serDispositivo.data)
    
    #============================================================================

class PersonaView(APIView):
    
    def get(self,request):
        dataPersona = Persona.objects.all()
        serPersona = PersonaSerializer(dataPersona,many=True)
        return Response(serPersona.data)
    
    def post(self,request):
        serPersona = PersonaSerializer(data=request.data)
        serPersona.is_valid(raise_exception=True)
        serPersona.save()
        
        return Response(serPersona.data)
    
class PersonaDetailView(APIView):
    
    def get(self,request,persona_id):
        dataPersona = Persona.objects.get(pk=persona_id)
        serPersona = PersonaSerializer(dataPersona)
        return Response(serPersona.data)
    
    def put(self,request,persona_id):
        dataPersona = Persona.objects.get(pk=persona_id)
        serPersona = PersonaSerializer(dataPersona,data=request.data)
        serPersona.is_valid(raise_exception=True)
        serPersona.save()
        return Response(serPersona.data)
    
    def delete(self,request,persona_id):
        dataPersona = Persona.objects.get(pk=persona_id)
        serPersona = PersonaSerializer(dataPersona)
        dataPersona.delete()
        return Response(serPersona.data)
    
    #============================================================================

class DetalleAccesoView(APIView):
    
    def get(self,request):
        dataDetalleAcceso = DetalleAcceso.objects.all()
        serDetalleAcceso = DetalleAccesoSerializer(dataDetalleAcceso,many=True)
        return Response(serDetalleAcceso.data)
    
    def post(self,request):
        serDetalleAcceso = DetalleAccesoSerializer(data=request.data)
        serDetalleAcceso.is_valid(raise_exception=True)
        serDetalleAcceso.save()
        
        return Response(serDetalleAcceso.data)
    
class DetalleAccesoDetailView(APIView):
    
    def get(self,request,detalle_acceso_id):
        dataDetalleAcceso = DetalleAcceso.objects.get(pk=detalle_acceso_id)
        serDetalleAcceso = DetalleAccesoSerializer(dataDetalleAcceso)
        return Response(serDetalleAcceso.data)
    
    def put(self,request,detalle_acceso_id):
        dataDetalleAcceso = DetalleAcceso.objects.get(pk=detalle_acceso_id)
        serDetalleAcceso = DetalleAccesoSerializer(dataDetalleAcceso,data=request.data)
        serDetalleAcceso.is_valid(raise_exception=True)
        serDetalleAcceso.save()
        return Response(serDetalleAcceso.data)
    
    def delete(self,request,detalle_acceso_id):
        dataZona = Zona.objects.get(pk=detalle_acceso_id)
        serZona = ZonaSerializer(dataZona)
        dataZona.delete()
        return Response(serZona.data)
    
    #============================================================================

class AccesoView(APIView):
    
    def get(self,request):
        dataAcceso = Acceso.objects.all()
        serAcceso = AccesoSerializer(dataAcceso,many=True)
        return Response(serAcceso.data)
    
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
    
    #============================================================================

class RolView(APIView):
    
    def get(self,request):
        dataRol = Rol.objects.all()
        serRol = RolSerializer(dataRol,many=True)
        return Response(serRol.data)
    
    def post(self,request):
        serRol = RolSerializer(data=request.data)
        serRol.is_valid(raise_exception=True)
        serRol.save()
        
        return Response(serRol.data)
    
class RolDetailView(APIView):
    
    def get(self,request,rol_id):
        dataRol = Rol.objects.get(pk=rol_id)
        serRol = RolSerializer(dataRol)
        return Response(serRol.data)
    
    def put(self,request,rol_id):
        dataRol = Rol.objects.get(pk=rol_id)
        serRol = RolSerializer(dataRol,data=request.data)
        serRol.is_valid(raise_exception=True)
        serRol.save()
        return Response(serRol.data)
    
    def delete(self,request,rol_id):
        dataRol = Rol.objects.get(pk=rol_id)
        serRol = RolSerializer(dataRol)
        dataRol.delete()
        return Response(serRol.data)
    
    #============================================================================

class ConfiguracionView(APIView):
    
    def get(self,request):
        dataConfiguracion = Configuracion.objects.all()
        serConfiguracion = ConfiguracionSerializer(dataConfiguracion,many=True)
        return Response(serConfiguracion.data)
    
    def post(self,request):
        serConfiguracion = ConfiguracionSerializer(data=request.data)
        serConfiguracion.is_valid(raise_exception=True)
        serConfiguracion.save()
        
        return Response(serConfiguracion.data)
    
class ConfiguracionDetailView(APIView):
    
    def get(self,request,configuracion_id):
        dataConfiguracion = Configuracion.objects.get(pk=configuracion_id)
        serConfiguracion = ConfiguracionSerializer(dataConfiguracion)
        return Response(serConfiguracion.data)
    
    def put(self,request,configuracion_id):
        dataConfiguracion = Configuracion.objects.get(pk=configuracion_id)
        serConfiguracion = ConfiguracionSerializer(dataConfiguracion,data=request.data)
        serConfiguracion.is_valid(raise_exception=True)
        serConfiguracion.save()
        return Response(serConfiguracion.data)
    
    def delete(self,request,configuracion_id):
        dataConfiguracion = Configuracion.objects.get(pk=configuracion_id)
        serConfiguracion = ConfiguracionSerializer(dataConfiguracion)
        dataConfiguracion.delete()
        return Response(serConfiguracion.data)
    
    #============================================================================

