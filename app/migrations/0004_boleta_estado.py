# Generated by Django 5.0.6 on 2024-07-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producto_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('enviado', 'Enviado'), ('entregado', 'Entregado')], default='pendiente', max_length=20),
        ),
    ]
