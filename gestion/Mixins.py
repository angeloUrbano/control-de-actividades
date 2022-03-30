from django.http import request
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from django.contrib import messages




class validarPermisosRequeridosMixin(object):

    permission_required = ''
    url_redirect = None

    def get_perms(self):

        if isinstance(self.permission_required , str):

            perms=(self.permission_required)

        else:

            perms= self.permission_required

        return perms    


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('gestion:lista_actividades')

        return self.self.url_redirect   

    def dispatch(self , request , *args , **kwargs):
        print(request.user)
        if request.user.has_perm(self.get_perms()):
            print("aquiiiiiiiiiiiiiii en el dispatch")
            return super().dispatch(request , *args , **kwargs)
        print("aquiiiiiiiiiiiiiii no esyoy en  el dispatch")
        messages.error(request, 'no tiene permitido el acceso')    
        return redirect(self.get_url_redirect())    


