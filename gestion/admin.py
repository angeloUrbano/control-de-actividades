from django.contrib import admin

from django.contrib import admin
from .models import activ_principal, sud_actividad, User
from django.contrib.auth.models import Permission


class activ_principalAdmin(admin.ModelAdmin):

    search_fields=['nom_actividades',]
   
    list_display=('nom_actividades','indicadores','region')

 

class estadosAdmin(admin.ModelAdmin):

    search_fields=['nom_estado']



"""class profileAdmin(admin.ModelAdmin):


    search_fields=['nombre']"""
  






admin.site.site_header= "Sistema de Gestion de Atit"
admin.site.site_title= " Gestional Plan  de Fortalicimiento"
admin.site.index_title ="Corpolec"


admin.site.register(activ_principal, activ_principalAdmin)
admin.site.register(sud_actividad, estadosAdmin)


admin.site.register(User)

admin.site.register(Permission)

#admin.site.register(Profile, profileAdmin)

