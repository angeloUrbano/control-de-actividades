from django import forms
from django.db.models import fields
from django.forms import widgets
import re
from datetime import date, time, datetime


from .models  import  activ_principal, estados, sud_actividad
from django.core.exceptions import ValidationError

from .validators import letras_solo




class activ_principalForm(forms.ModelForm):

	class Meta:

		model=activ_principal

		fields=['num_actividades','nom_actividades','indicadores','costo','avance_1','alcance','region', 'id_estado2']

 

	
		labels={
			'num_actividades':'Nro  Actividad',
			'nom_actividades': 'Nom Actividad',
			'indicadores' :'Indicadores',
			'costo' : 'Costo',
			'avance_1' :'Avance',
			'alcance': 'Alcance',
			'region':'Region',
			'id_estado2':'Estado'
		}
			
				
				
		



		widgets = {

		'num_actividades': forms.NumberInput(attrs={'class':'form-control'}),
		'nom_actividades': forms.TextInput(attrs={'class':'form-control'}),
		'indicadores': forms.TextInput(attrs={'class':'form-control'}),
		'costo': forms.NumberInput(attrs={'class':'form-control'}),
		'avance_1': forms.NumberInput(attrs={'class':'form-control'}),
		'alcance':forms.TextInput(attrs={'class':'form-control'}),
		'region':forms.TextInput(attrs={'class':'form-control'}),
		'id_estado2': forms.Select(attrs={'class':'form-control'})

		}


	

  


class sud_actividadForm(forms.Form):

	num_actividad = forms.FloatField()

	nom_actividad = forms.CharField()

	fecha_inicio = forms.DateField()
	fecha_fin = forms.DateField()
	fecha_real = forms.DateField()
	impacto =forms.CharField(max_length=500 , required=False)
	punto_critico = forms.CharField(max_length=500 , required=False)

	nom_actividad.widget.attrs.update({'class':'form-control'})
	

	def clean_nom_actividad(self):

		#patron = re.compile("^\w+$")
		nom_actividad = self.cleaned_data.get('nom_actividad')
		
		
		if not re.match(r'[a-zA-Z\s]+$', nom_actividad):
			print("no coniside")
			raise forms.ValidationError("debe ser solo letras")

		
		return nom_actividad

	def clean_impacto(self):

		#patron = re.compile("^\w+$")
		impacto = self.cleaned_data.get('impacto')
		
		
		if not re.match(r'[a-zA-Z\s]+$', impacto):
			print("no coniside")
			raise forms.ValidationError("debe ser solo letras")

		
		return impacto	

	def clean_punto_critico(self):

		#patron = re.compile("^\w+$")
		punto_critico = self.cleaned_data.get('punto_critico')
		
		
		if not re.match(r'[a-zA-Z\s]+$', punto_critico):
			print("no coniside")
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

	#valido fecha fin  real

	def clean_fecha_real(self):

		fecha_inicio= self.cleaned_data.get('fecha_inicio')
		fecha_real= self.cleaned_data.get('fecha_real')
		

		fecha_actual = date.today()
	

		if fecha_real == fecha_actual or fecha_real < fecha_actual or fecha_real == fecha_inicio:

			raise ValidationError("Debe ingresar una fecha correcta")

		return fecha_real	


		
			
			
			
		
		

    
		
		
	
#este lo uso en editar 
class sud_actividadForm2(forms.ModelForm):


	class Meta:

		model= sud_actividad
		fields= ['num_actividad','nom_actividad','fecha_inicio','fecha_fin','fecha_real','impacto','punto_critico']




		labels={

			'Num actividad':'num_actividad',
			'Nombre actividad':'nom_actividad',
			'fecha inicio': 'fecha_inicio',
			'fecha fin': 'fecha_fin',
			'fecha real':'fecha_real',
			'impacto':'impacto',
			'punto critico':'punto_critico'
			

		}

		widgets = {
			
			'num_actividad': forms.NumberInput(attrs={'class':'form-control'}),
			'nom_actividad':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inicio': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_fin': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'fecha_real': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
			'impacto':forms.TextInput(attrs={'class':'form-control'}),
			'punto_critico':forms.TextInput(attrs={'class':'form-control'}),
			

		}




	def clean_nom_actividad(self):

		#patron = re.compile("^\w+$")
		nom_actividad = self.cleaned_data.get('nom_actividad')
		
		
		if not re.match(r'[a-zA-Z\s]+$', nom_actividad):
			print("no coniside")
			raise forms.ValidationError("debe ser solo letras")

		
		return nom_actividad

	def clean_impacto(self):

		#patron = re.compile("^\w+$")
		impacto = self.cleaned_data.get('impacto')
		
		
		if not re.match(r'[a-zA-Z\s]+$', impacto):
			print("no coniside")
			raise forms.ValidationError("debe ser solo letras")

		
		return impacto	

	def clean_punto_critico(self):

		#patron = re.compile("^\w+$")
		punto_critico = self.cleaned_data.get('punto_critico')
		
		
		if not re.match(r'[a-zA-Z\s]+$', punto_critico):
			print("no coniside")
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

	#valido fecha fin  real

	def clean_fecha_real(self):

		fecha_inicio= self.cleaned_data.get('fecha_inicio')
		fecha_real= self.cleaned_data.get('fecha_real')
		

		fecha_actual = date.today()
	

		if fecha_real == fecha_actual or fecha_real < fecha_actual or fecha_real == fecha_inicio:

			raise ValidationError("Debe ingresar una fecha correcta")

		return fecha_real	


			


