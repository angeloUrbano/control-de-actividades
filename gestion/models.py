from django.db import models


from django.contrib.admin.filters import ChoicesFieldListFilter
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DecimalField

from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Profile(models.Model):
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



class estados (models.Model):

    id_estado =models.AutoField(primary_key=True)
    nom_estado  = models.CharField('Nombre Estado',max_length=100, blank=False, null=True) 



    def __str__(self):
        return self. nom_estado


    class Meta:
        verbose_name='estado'
        verbose_name_plural='estados'
        ordering = ['nom_estado']






                                                                                                                                                                                                                                            

    

class activ_principal(models.Model):

    id =models.AutoField(primary_key=True)
    num_actividades = models. IntegerField(blank=False, null=True)
    nom_actividades = models.TextField('Actividad a realizar',blank=False, null=True)
    indicadores = models.TextField(blank=True, null=False)
    costo = models.FloatField('Costo de la actividad', blank=True, null=True)
    avance_1 = models.FloatField('avance Programado',blank= True, null=True)
    
    alcance = models.TextField('Alcance',blank=False , null=True)
    region = models.CharField ('Region',max_length=100, blank=True, null= True)
    id_estado2 =  models.ForeignKey(estados, blank=False, null= True, on_delete=models.CASCADE )


    
     
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



