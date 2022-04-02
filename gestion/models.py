from django.db import models


from django.contrib.admin.filters import ChoicesFieldListFilter
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DecimalField

from django.contrib.auth.models import User
from django.core.validators import RegexValidator


from django.contrib.auth.models import AbstractUser


STATE_CHOICES = (
    ('Amazonas', 'Amazonas'),
    ('Anzoátegui', 'Anzoátegui'),
	('Apure', 'Apure'),
	('Aragua', 'Aragua'),
	('Barinas', 'Barinas'),
	('Bolívar', 'Bolívar'),
	('Carabobo', 'Carabobo'),
	('Cojedes', 'Cojedes'),
	('Delta Amacuro', 'Delta Amacuro'),
	('Distrito' , 'Distrito'),
	('Falcón', 'Falcón'),
	('Guárico', 'Guárico'),
	('Lara', 'Lara'),
	('Mérida', 'Mérida'),
	('Miranda', 'Miranda'),
	('Monagas', 'Monagas'),
	('Nueva Esparta', 'Nueva Esparta'),
	('Portuguesa' , 'Portuguesa'),
	('Sucre', 'Sucre'),
	('Táchira' , 'Táchira'),
	('Trujillo', 'Trujillo'),
	('Vargas', 'Vargas'),
	('Yaracuy', 'Yaracuy'),
	('Zulia', 'Zulia')
)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    cedula = models.CharField(max_length=100 , blank=False, null= False)
    nombre_corporativo = models.CharField(max_length=100 , blank=False, null= False)
    estado = models.CharField(choices=STATE_CHOICES, max_length=20 , blank=False, null= False)
    cargo= models.CharField(max_length=100 , blank=False, null= False )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[ 'username',  'first_name' , 'last_name'  , 'cedula' , 'nombre_corporativo' , 
    'estado' , 'cargo' ]

    


   





    def __str__(self):
        return '{}'.format(self.email)



"""class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   nombre = models.CharField(max_length= 50)
   apellido = models.CharField(max_length= 50)
   email = models.EmailField()
   region = models.CharField(max_length=30)
   nivel = models.IntegerField()
   create = models.DateTimeField(auto_now_add=True)
   modified= models.DateTimeField(auto_now= True)

   def __str__(self):
      return '{}'.format(self.user.username) 
"""


"""class estados (models.Model):

    id_estado =models.AutoField(primary_key=True)
    nom_estado  = models.CharField('Nombre Estado',max_length=100, blank=False, null=True) 



    def __str__(self):
        return self. nom_estado


    class Meta:
        verbose_name='estado'
        verbose_name_plural='estados'
        ordering = ['nom_estado']"""






                                                                                                                                                                                                                                            

  

class activ_principal(models.Model):

    id =models.AutoField(primary_key=True)
    num_actividades = models. IntegerField(blank=False, null=True)
    nom_actividades = models.TextField('Actividad a realizar',blank=False, null=True)
    indicadores = models.TextField(blank=True, null=False)
    costo = models.FloatField('Costo de la actividad', blank=True, null=True)
    avance_1 = models.FloatField('avance Programado',blank= True, null=True)
    
    alcance = models.TextField('Alcance',blank=False , null=True)
    region = models.CharField ('Region',max_length=100, blank=True, null= True)
    id_estado2 =  models.CharField(choices=STATE_CHOICES, max_length=20 , blank=False, null= False)


    
     
    class Meta:
        verbose_name='actividad'
        verbose_name_plural='actividades'


        



    def  __str__(self):
        return self.nom_actividades

    




class  sud_actividad(models.Model):
    
    num_actividad = models.FloatField()
    nom_actividad = models.CharField( max_length=500 ,   blank=False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_real = models.DateField()
    impacto = models.CharField( max_length=500, blank=False, null= True)
    punto_critico = models.CharField( max_length=500 , blank= False, null=True) 
    id_activ = models.ForeignKey(activ_principal, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    def  __str__(self):
        return self.nom_actividad


    class Meta:
        verbose_name=' Sud_actividad'
        verbose_name_plural='Sud_actividades'



