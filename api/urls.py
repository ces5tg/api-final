from django.urls import path

from . import views





urlpatterns = [
 
    path('',views.IndexView.as_view(),name='index'),
    path('zona',views.ZonaView.as_view(),name='zona'),
    path('zona/<int:zona_id>',views.ZonaDetailView.as_view()),

    path('tipo_aula',views.TipoAulaView.as_view(),name='tipo_aula'),
    path('tipo_aula/<int:tipo_aula_id>',views.TipoAulaDetailView.as_view()),

    path('aula',views.AulaView.as_view(),name='aula'),
    path('aula/<int:aula_id>',views.AulaDetailView.as_view()),

    path('dispositivos',views.DispositivoView.as_view(),name='dispositivos'),
    path('dispositivos/<int:dispositivos_id>',views.DispositivoDetailView.as_view()),

    path('personal',views.PersonaView.as_view(),name='personal'),
    path('personal/<int:personal_id>',views.PersonaDetailView.as_view()),

    path('detalle_acceso',views.DetalleAccesoView.as_view(),name='detalle_acceso'),
    path('detalle_acceso/<int:detalle_acceso_id>',views.DetalleAccesoDetailView.as_view()),

    path('acceso',views.AccesoView.as_view(),name='acceso'),
    path('acceso/<int:acceso_id>',views.AccesoDetailView.as_view()),

    path('rol',views.RolView.as_view(),name='rol'),
    path('rol/<int:rol_id>',views.RolDetailView.as_view()),

    path('configuracion',views.ConfiguracionView.as_view(),name='configuracion'),
    path('configuracion/<int:configuracion_id>',views.ConfiguracionDetailView.as_view()),

  
   
]
