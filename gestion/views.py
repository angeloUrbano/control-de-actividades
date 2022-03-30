

from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse

from django.views.generic.edit import DeleteView, UpdateView
from openpyxl.styles.fills import FILL_NONE

from gestion.forms import activ_principalForm, sud_actividadForm , sud_actividadForm2 , Crea_Usuario
from gestion.models import *
from gestion.Mixins import validarPermisosRequeridosMixin
from django.contrib.auth import authenticate, get_user_model

from django.views.generic import View, UpdateView, CreateView,  DetailView, TemplateView , ListView , DeleteView
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

from django.urls import  reverse_lazy


from  openpyxl import Workbook, workbook
from openpyxl.styles import  PatternFill, Border, Side, Alignment, Protection, Font, alignment
from django.http.response import HttpResponse, StreamingHttpResponse




from django.contrib.auth.mixins import PermissionRequiredMixin




     
      

def login_view(request):
	
	print(request.POST)
	if request.method== 'POST':
		
		
		username = request.POST['email']
		password = request.POST['password']
	
		User = authenticate( username=username, password = password)
        
		print(User)
		if User :
			
			login(request , User)
           
			
			return redirect('gestion:lista_actividades')
		else:
			return render(request , "corp/login.html" , {'error': 'Correo o Contraseña Invalido'})	
	return render(request , "corp/login.html")


@login_required
def logout_view(request):
	logout(request)
	return redirect('login')    






class crear_usuario(View):

   
    template_name = 'corp/signup.html'
    form_class = Crea_Usuario




    def get (self, request):

        return render(request,self.template_name , {'form':self.form_class})


    def post(self , request , *args , **kwargs):

        form  = self.form_class(request.POST) 
        

        if form.is_valid():
            print("aquiii ya pase el formularo valido")

         

            datos_limpios = form.cleaned_data

          

           

           
            email = datos_limpios['email']
            first_name = datos_limpios['first_name']
            last_name = datos_limpios['last_name']
            password = datos_limpios['password']
            password_confirmation = datos_limpios['password_confirmation']
            cedula= datos_limpios['cedula']
            nombre_corporativo= datos_limpios['nombre_corporativo']
            estado= datos_limpios['estado']
            cargo = datos_limpios['cargo']
            

            User = get_user_model()
            User = User.objects.create_user(username=first_name, email=email , last_name =last_name , password = password , is_active = True ,
            cedula =cedula , nombre_corporativo = nombre_corporativo , estado =estado ,
            cargo = cargo)
            for x in datos_limpios['groups']:

                User.groups.add(x)



            """User.set_password(password)
            User.is_active = True
            User.save()"""
            return redirect('gestion:lista_actividades')

        return render(request , self.template_name , {'form':form})



	




class signup (View):

    def get (self, request):

        return render(request,'corp/signup.html')

    def post(self,request):

        username = request.POST['username']
        email = request.POST['username']

        
        nombre = request.POST['Nombre']
        last_name = request.POST['last_name']
        region = request.POST['estado']
        nivel = request.POST['nivel']
        

        
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        context = {
            'fieldValues': request.POST
        }


        if password != password_confirmation:

            print('contraseña')

            return render (request, 'corp/signup.html', {'error': 'Contraseñas no coinciden'})
        
        User = get_user_model()

        if User.objects.filter(email =email).exists():
            return render (request, 'corp/signup.html', {'error': 'Correo en uso'})

        if not User.objects.filter(email=email).exists():

          User = User.objects.create_user(username=username, email=email)
          User.set_password(password)
          User.is_active = True
          User.save()


          print("!!!!!!!!!!!!!!!!!! porque no se guarda!!!!!!!!!!!!!!")
          profile= Profile( user=User, nombre=nombre , apellido=apellido , email=email, region=region, nivel=nivel)
          print("!!!!!!!!!!!!!!!!se guardo!!!!!!!!!!!!!!!!")
          profile.save

          return redirect('login')


        return render(request, 'corp/signup.html')






"""
    ##############

            COMIENZO DESDE CERO

                            ###########################

                    """
  

class muestra (TemplateView):

    template_name="corp/registro2.html"



class crear_actividad (CreateView):
   
  
    model = activ_principal
    template_name = "corp/registro2.html"
    form_class =  activ_principalForm
    success_url = reverse_lazy('gestion:lista_actividades')



class crear_sud_actividad(View):
   
    model =  sud_actividad
    second_model= activ_principal
    template_name = "corp/registro1.html"
    form_class =  sud_actividadForm
    success_url = reverse_lazy('gestion:lista_actividades')


    #esta funcion me permite agarrar el valor de id de la actividad que viene en la url
    # con esto lo agarro self.kwargs['pk']
    def get_object(self , **kwargs):

        
        var = self.second_model.objects.get(id=self.kwargs['pk'])		

        return var


    """
    esta funcion me permire reescribir el metodo post de mi clase y lo uso para guardar la sub actividad 
    lo hago asi por que quiero que el cliente no tenga necesidad de seleccionar a que actividad
    pertenece esta sub actividad 
    entonces con la funcion  get_object me traigo el objeto  que es la actividad para tener ese valor por defecto
    y asi el cliente no tendra que buscar pot ejemplo entre 1.000 actividades 
    para ver cual es la suya o cosas por el estilo"""

    def post(self , request , *args , **kwargs) :

        form = self.form_class(request.POST)

        if form.is_valid():
            
            #le quito el html al formulario que viene por el metodo post 
            formulario_limpio = form.cleaned_data


            #creo un objeto de mi modelo para usarlo para guardar 
            sub_actividad_guuardar = self.model()

            #accedo a las propiedades de mi objeto
            sub_actividad_guuardar.num_actividad = formulario_limpio['num_actividad']
            sub_actividad_guuardar.nom_actividad= formulario_limpio['nom_actividad']
            sub_actividad_guuardar.fecha_inicio = formulario_limpio['fecha_inicio']
            sub_actividad_guuardar.fecha_fin = formulario_limpio['fecha_fin']
            sub_actividad_guuardar.fecha_real = formulario_limpio['fecha_real']
            sub_actividad_guuardar.impacto = formulario_limpio['impacto']
            sub_actividad_guuardar.punto_critico = formulario_limpio['punto_critico']
            sub_actividad_guuardar.id_activ = self.get_object()

            sub_actividad_guuardar.save()

            #reverse contruye una url  lo uso ya que redirec no permite kwargs
            url = reverse('gestion:detalle_actividad' , kwargs={'pk':self.kwargs['pk']})
			
            return redirect(url)

        
        print(form.errors)
            
        return render(request, 'corp/editar_subActividad.html' , {'form':form , 'object': self.get_object})
        
            

    def get_context_data(self , **kwargs):

        context= {}
	
        context['form']=self.form_class
        context['object']= self.get_object()
		
        return context



    def  get(self , request , *args , **kwargs):
		


        return render(request , self.template_name , self.get_context_data())        
            







class lista_actividades(ListView):
    
    model = activ_principal
    template_name = "corp/listar_actividad.html"




class editar_actividad(UpdateView):
    model= activ_principal
    form_class =  activ_principalForm
    template_name="corp/modal_editar_actividad.html"
    #fields=['num_actividades','nom_actividades','indicadores','costo','avance_1','alcance','region', 'id_estado2']  
    success_url = reverse_lazy('gestion:lista_actividades')
    

#validarPermisosRequeridosMixin es un validador de permisos creado por mi y esta en Mixins.py
class eliminar_actividad(validarPermisosRequeridosMixin , DeleteView):
    permission_required = 'gestion.delete_activ_principal'
    model = activ_principal

    template_name="corp/eliminar_actividad.html"
    success_url = reverse_lazy('gestion:lista_actividades')



class detalle_actividad(DetailView):
    second_model = sud_actividad
   
    template_name= 'corp/detalle_actvidad.html'
    pk_url_kwargs= 'pk'	
    queryset= activ_principal.objects.all()


    """
    las primeras lineas me traen solo la actividad que selecciono al darle al boton
     detalle en la lista de actividades
    y la siguiente funcion a continuacion lo que hago es traerme las actividades
     a de esa actividad y mardarlas al templete para
    listarlas"""

    def get_context_data(self , **kwargs):

        context = super().get_context_data(**kwargs)
        
        datos = self.second_model.objects.filter(id_activ=self.kwargs['pk'])

        context['info']= datos

        return context


class editar_sub_actividad(UpdateView):

    model= sud_actividad
    form_class = sud_actividadForm2   
    template_name="corp/editar_subActividad.html"
    def post(self , request , *args , **kwargs):

        instancia = self.model.objects.get(id=self.kwargs['pk'])
        form = self.form_class(request.POST , instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

            url = reverse('gestion:detalle_actividad' , kwargs={'pk':self.kwargs['pk2']})
            return redirect(url)

        return render(request , self.template_name , {'form':form})    
    

    

#validarPermisosRequeridosMixin es un validador de permisos creado por mi y esta en Mixins.py 
class eliminar_sub_Actividad(validarPermisosRequeridosMixin , DeleteView):
    permission_required = 'gestion.delete_sud_actividad'
    model = sud_actividad
    template_name="corp/eliminar_subActividad.html"
    success_url = reverse_lazy('gestion:lista_actividades') 



    def post(self , request , *args , **kwargs):

        instancia = self.model.objects.get(id=self.kwargs['pk'])
        
        
        instancia.delete()
           

        url = reverse('gestion:detalle_actividad' , kwargs={'pk':self.kwargs['pk2']})
        return redirect(url)





class listar_user(ListView):

    model = User
    template_name = 'corp/lista_user.html'
    


        







        

    



