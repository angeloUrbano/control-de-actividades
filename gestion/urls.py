from django.urls import  path

from .views import *




urlpatterns = [
    
     path("prueba/", crear_actividad.as_view(), name="prueba"),
    
     path("lista_actividades/" , lista_actividades.as_view() , name="lista_actividades"),
     path("editar_actividad/<int:pk>/", editar_actividad.as_view(), name= "editar_actividads"),
     path("eliminar_actividad/<int:pk>/" , eliminar_actividad.as_view() , name="eliminar_actividad"),
     path("detalle_actividad/<int:pk>/" , detalle_actividad.as_view() , name= "detalle_actividad"),


    path("crea_sub_actividad/<int:pk>" , crear_sud_actividad.as_view() , name="crea_sub_actividad"),
    path("editar_subActividad/<int:pk>/<int:pk2>/" , editar_sub_actividad.as_view() , name= "editar_subActividad"),
    path("eliminar_subActividad/<int:pk>/<int:pk2>/" , eliminar_sub_Actividad.as_view() , name= "eliminar_subActividad"),


    path("crear_user/", crear_usuario.as_view(), name="crear_user"),
    path("listar_usiarios/", listar_user.as_view(), name="listar_usiarios"),
    
 
    
]
