# Generated by Django 4.0.1 on 2022-03-25 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='activ_principal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_actividades', models.IntegerField(null=True)),
                ('nom_actividades', models.TextField(null=True, verbose_name='Actividad a realizar')),
                ('indicadores', models.TextField(blank=True)),
                ('costo', models.FloatField(blank=True, null=True, verbose_name='Costo de la actividad')),
                ('avance_1', models.FloatField(blank=True, null=True, verbose_name='avance Programado')),
                ('alcance', models.TextField(null=True, verbose_name='Alcance')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region')),
            ],
            options={
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='estados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nom_estado', models.CharField(max_length=100, null=True, verbose_name='Nombre Estado')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'ordering': ['nom_estado'],
            },
        ),
        migrations.CreateModel(
            name='sud_actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_actividad', models.FloatField()),
                ('nom_actividad', models.CharField(max_length=500)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('fecha_real', models.DateTimeField()),
                ('impacto', models.CharField(max_length=500, null=True)),
                ('punto_critico', models.CharField(max_length=500, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_activ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.activ_principal')),
            ],
            options={
                'verbose_name': ' Sud_actividad',
                'verbose_name_plural': 'Sud_actividades',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=30)),
                ('nivel', models.IntegerField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activ_principal',
            name='id_estado2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.estados'),
        ),
    ]
