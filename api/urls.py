from django.urls import path , include

from .views import *
from . import views
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('zona' , ZonaViewSet)
router.register('tipo_aula' , TipoAulaViewSet)
router.register('aula' , AulaViewSet)
router.register('dispositivo' , DispositivoViewSet)
router.register('persona' , PersonaViewSet)
router.register('detalleAcceso' , DetalleAccesoViewSet)
router.register('acceso' , AccesoViewSet)
router.register('rol' , RolViewSet)
router.register('configuracion' ,ConfiguracionViewSet)




urlpatterns = [
 
    #path('',views.IndexView.as_view(),name='index'),
    path('' , include(router.urls)),
   path('api/mi_vista/', views.mi_vista),
  
   
]
