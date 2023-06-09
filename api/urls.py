from django.urls import path

from . import views

urlpatterns = [
 
    path('',views.IndexView.as_view(),name='index'),
    path('acceso',views.AccesosView.as_view(),name='series'),
    path('acceso/<int:accesp_id>',views.AccesoDetailView.as_view()),
   
]
