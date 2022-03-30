from django.shortcuts import redirect
from django.urls import  reverse_lazy




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
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request , *args , **kwargs)
        return redirect(self.get_url_redirect())    


