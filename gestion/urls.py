from django.urls import  path

from .views import *


reporte_excel

urlpatterns = [

    path("genera_reportes/", genera_reporte.as_view(), name="genera_reportes"),
    path("muestra_graficas/", muestra_grafica.as_view(), name="muestra_graficas"),
    path("frmulario_estadist/", formulario_estadistica.as_view(), name="frmulario_estadist"),
 


    path("reporte/", reporte_excel.as_view(), name="reporte"),
    
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
    path("detalle_usiarios/<int:pk>", detalle_Usuario.as_view(), name="detalle_usiarios"),
    path("editar_usiarios/<int:pk>", editar_usuario.as_view(), name="editar_usiarios"),
    path("editarcontraseña_usiarios/<int:pk>", editar_contraseña_usuario.as_view(), name="editarcontraseña_usiarios"),
    path("eliminar_usiarios/<int:pk>", eliminar_Usuario.as_view(), name="eliminar_usiarios"),

    path("reporte/" , reporte_excel.as_view() , name="reporte"),    
    
 
    
]
