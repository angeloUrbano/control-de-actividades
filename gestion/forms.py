from django import forms
from django.db.models import fields
from django.forms import widgets
import re
from django.contrib.auth.models import User
from datetime import date, time, datetime


from .models  import  activ_principal,  sud_actividad
from django.core.exceptions import ValidationError

from .validators import letras_solo



from django.contrib.auth import get_user_model


class update_contraseña_Usuario(forms.ModelForm):
	
	password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput(
		attrs={'class':'form-control'}
	))


	class Meta:
		User = get_user_model()

		model=User
	

		fields=['password']

		


		labels={
			'password':'password'
		}


		widgets = {

		

		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		
		}




	def clean(self):
		data = super().clean()

		password= data['password']
		password_confirmation = data['password_confirmation']
		
		
		
		if password != password_confirmation:
			raise forms.ValidationError('Las contrañas no coninciden ')

		
				

		if  not password.isalnum()  or  not password_confirmation.isalnum() :
			raise forms.ValidationError('la contraseña debe estar conpuesta de numeros y letras y tener un maximo de 8 caracteres')



		return data	







class update_Usuario(forms.ModelForm):
	
	

	class Meta:
		User = get_user_model()

		model=User
	

		fields=['email','first_name','last_name','groups'  ,
		'cedula' ,'username' , 'estado'  , 'cargo' ]

		


		labels={
			'email':'correo',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'cedula': 'Cedula',
			'username' :'Nombre Corporativo' ,
			'estado':'Estado',
			'cargo':'Cargo',
			'groups':'gupos'

			
		}


		widgets = {

		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),

		'cedula': forms.TextInput(attrs={'class':'form-control'}),
		'username': forms.TextInput(attrs={'class':'form-control'}),
		'estado': forms.Select(attrs={'class':'form-control'}),
		'cargo': forms.TextInput(attrs={'class':'form-control'}),


		'groups': forms.SelectMultiple(attrs={'class':'form-control'}),

		
		
		}



class Crea_Usuario(forms.ModelForm):
	
	password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput(
		attrs={'class':'form-control'}
	))


	class Meta:
		User = get_user_model()

		model=User
	

		fields=['email','first_name','last_name','groups'  ,
		'cedula' ,'nombre_corporativo' , 'estado'  , 'cargo' , 'password']

		


		labels={
			'email':'correo',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'cedula': 'Cedula',
			'nombre_corporativo' :'Nombre Corporativo' ,
			'estado':'Estado',
			'cargo':'Cargo',
			'groups':'gupos',

			'password':'password'
		}


		widgets = {

		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),

		'cedula': forms.TextInput(attrs={'class':'form-control'}),
		'nombre_corporativo': forms.TextInput(attrs={'class':'form-control'}),
		'estado': forms.Select(attrs={'class':'form-control'}),
		'cargo': forms.TextInput(attrs={'class':'form-control'}),


		'groups': forms.SelectMultiple(attrs={'class':'form-control'}),

		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		
		}

	
	def clean_groups(self):

		#patron = re.compile("^\w+$")
		groups = self.cleaned_data.get('groups')
		
		
		if  not groups:
			
			raise forms.ValidationError("debe asignarle un nivel al usuario ")

		
		return groups
	

	def clean_first_name(self):

		#patron = re.compile("^\w+$")
		first_name = self.cleaned_data.get('first_name')
		
		
		if not re.match(r'[a-zA-Z\s]+$', first_name) or first_name == "":
			
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")

		
		return first_name


	def clean_last_name(self):

		#patron = re.compile("^\w+$")
		last_name = self.cleaned_data.get('last_name')
		
		
		if not re.match(r'[a-zA-Z\s]+$', last_name) or last_name == "":
			
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")

		
		return last_name


	def clean_cedula(self):

		#patron = re.compile("^\w+$")
		cedula = self.cleaned_data.get('cedula')
		
		
		if not re.match(r'\d+$', cedula) or len(cedula)>8:
			
			raise forms.ValidationError("Error! solo debe ser numero y un maximo de 8 caracteres")

		else:
			User = get_user_model()
			if User.objects.filter(cedula =cedula).exists():
				
				
				raise forms.ValidationError("Error! la cedula ya se encuentra en uso")	

		
		return cedula	

	def clean_nombre_corporativo(self):

		#patron = re.compile("^\w+$")
		nombre_corporativo = self.cleaned_data.get('nombre_corporativo')

		User = get_user_model()
		if User.objects.filter(username =nombre_corporativo).exists():
			raise forms.ValidationError("Nombre corporativo se encuenta en uso ")
		
		
		if not re.match(r'[a-zA-Z\s]+$', nombre_corporativo) or nombre_corporativo == "":
			
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")

		
		return nombre_corporativo	



	def clean_cargo(self):

		#patron = re.compile("^\w+$")
		cargo = self.cleaned_data.get('cargo')
		
		
		if not re.match(r'[a-zA-Z\s]+$', cargo) or cargo == "":
			
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")

		
		return cargo




		
	
	
	"""The problem is that User refers to django.contrib.auth.models.User 
	and now you have got a Custom User pet.Person assuming you have in the settings.py
	you have to define User with the Custom User model and you can do this with
	get_user_model at the top of the file where you use User"""

	User = get_user_model()
	def clean_email(self):

		email = self.cleaned_data['email']
		q = self.User.objects.filter(email=email).exists()
		if q:
		
			raise forms.ValidationError('Email ya esta en uso') 

		return email	

		

	def clean(self):
		data = super().clean()

		password= data['password']
		password_confirmation = data['password_confirmation']
		
		
		
		if password != password_confirmation:
			raise forms.ValidationError('Las contrañas no coninciden ')

		

	def save(self):
		#esta funcion es para guardar los datos
		data = self.cleaned_data
		data.pop('password_confirmation')#este campo es para eliminar por que no lo necesito
		user= User.objects.create_user(**data)
		profile= Profile(user=user)
		profile.save()



class activ_principalForm(forms.ModelForm):

	class Meta:

		model=activ_principal

		fields=['num_actividades','nom_actividades','indicadores','alcance','region', 'id_estado2'  , 'creado']

 

	
		labels={
			'num_actividades':'Numero  Actividad',
			'nom_actividades': 'Nombre Actividad',
			'indicadores' :'Indicadores',
			'alcance': 'Alcance',
			'region':'Region',
			'id_estado2':'Estado',
			'creado' : 'Fecha de creacion de actividad'
		}
			
				
				
		



		widgets = {

		'num_actividades': forms.NumberInput(attrs={'class':'form-control'}),
		'nom_actividades': forms.TextInput(attrs={'class':'form-control'}),
		'indicadores': forms.TextInput(attrs={'class':'form-control'}),
		'creado': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
		
		'alcance':forms.TextInput(attrs={'class':'form-control'}),
		'region':forms.Select(attrs={'class':'form-control'}),
		'id_estado2': forms.Select(attrs={'class':'form-control'})

		}


	

  


#este lo uso en editar 
class sud_actividadForm(forms.ModelForm):


	class Meta:

		model= sud_actividad
		fields= ['num_actividad','nom_actividad','fecha_inicio','fecha_fin', 'fecha_fin_real','impacto','punto_critico' ,  'avance_programado' , 'avance_ejecutado']




		labels={

			'Num actividad':'num_actividad',
			'Nombre actividad':'nom_actividad',
			'fecha inicio': 'fecha_inicio',
			'fecha fin': 'fecha_fin',
			'fecha fin real': 'fecha_fin_real',
			'impacto':'impacto',
			'punto critico':'punto_critico',
			'avance_programado':'Avance Programado',
			'avance_ejecutado' : 'Avance Ejecutado'
			

		}

		widgets = {
			
			'num_actividad': forms.NumberInput(attrs={'class':'form-control'}),
			'nom_actividad':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inicio': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_fin': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_fin_real': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'impacto':forms.Textarea(attrs={'class':'form-control'}),
			'punto_critico':forms.TextInput(attrs={'class':'form-control'}),
			'avance_programado': forms.NumberInput(attrs={'class':'form-control'}),
			'avance_ejecutado' :forms.NumberInput(attrs={'class':'form-control'}),
			

		}




	def clean_nom_actividad(self):

		#patron = re.compile("^\w+$")
		nom_actividad = self.cleaned_data.get('nom_actividad')
		
		
		if not re.match(r'[a-zA-Z\s]+$', nom_actividad):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return nom_actividad

	def clean_impacto(self):

		#patron = re.compile("^\w+$")
		impacto = self.cleaned_data.get('impacto')
		
		
		if not re.match(r'[a-zA-Z\s]+$', impacto):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return impacto	

	def clean_punto_critico(self):

		#patron = re.compile("^\w+$")
		punto_critico = self.cleaned_data.get('punto_critico')
		
		
		if not re.match(r'[a-zA-Z\s]+$', punto_critico):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return punto_critico




		


	


		
			
			
			
		
		

    
		
		
	
#este lo uso en editar 
class sud_actividadForm2(forms.ModelForm):


	class Meta:

		model= sud_actividad
		fields= ['num_actividad','nom_actividad','fecha_inicio','fecha_fin', 'fecha_fin_real','impacto','punto_critico' ,  'avance_programado' , 'avance_ejecutado']




		labels={

			'Num actividad':'num_actividad',
			'Nombre actividad':'nom_actividad',
			'fecha inicio': 'fecha_inicio',
			'fecha fin': 'fecha_fin',
			'fecha fin real': 'fecha_fin_real',
			'impacto':'impacto',
			'punto critico':'punto_critico',
			'avance_programado':'Avance Programado',
			'avance_ejecutado' : 'Avance Ejecutado'
			

		}

		widgets = {
			
			'num_actividad': forms.NumberInput(attrs={'class':'form-control'}),
			'nom_actividad':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inicio': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_fin': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_fin_real': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'impacto':forms.Textarea(attrs={'class':'form-control'}),
			'punto_critico':forms.TextInput(attrs={'class':'form-control'}),
			'avance_programado': forms.NumberInput(attrs={'class':'form-control'}),
			'avance_ejecutado' :forms.NumberInput(attrs={'class':'form-control'}),
			

		}




	def clean_nom_actividad(self):

		#patron = re.compile("^\w+$")
		nom_actividad = self.cleaned_data.get('nom_actividad')
		
		
		if not re.match(r'[a-zA-Z\s]+$', nom_actividad):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return nom_actividad

	def clean_impacto(self):

		#patron = re.compile("^\w+$")
		impacto = self.cleaned_data.get('impacto')
		
		
		if not re.match(r'[a-zA-Z\s]+$', impacto):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return impacto	

	def clean_punto_critico(self):

		#patron = re.compile("^\w+$")
		punto_critico = self.cleaned_data.get('punto_critico')
		
		
		if not re.match(r'[a-zA-Z\s]+$', punto_critico):
			
			raise forms.ValidationError("debe ser solo letras")

		
		return punto_critico



	#valido fecha inicio
	def clean_fecha_inicio(self):

		fecha_inicio= self.cleaned_data.get('fecha_inicio')
		fecha_actual = date.today()
		

		if  fecha_inicio < fecha_actual :

			raise ValidationError("Debe ingresar una fecha correcta")

		return fecha_inicio	


	#valido fecha fin 

	def clean_fecha_fin(self):

		fecha_inicio= self.cleaned_data.get('fecha_inicio')
		fecha_fin= self.cleaned_data.get('fecha_fin')
		

		fecha_actual = date.today()
	

		if fecha_fin == fecha_actual or fecha_fin < fecha_actual or fecha_fin == fecha_inicio:

			raise ValidationError("Debe ingresar una fecha correcta")

		return fecha_fin

	

	


			


