# Generated by Django 4.0.1 on 2022-03-29 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]