# Generated by Django 5.0.6 on 2024-06-25 23:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_u', models.CharField(max_length=50)),
                ('gmail', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('foto_perfil', models.ImageField(upload_to='editar_perfil', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_p', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='add_producto', verbose_name='Imagen')),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=50)),
                ('valor', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)])),
                ('detalle', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Historial_c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('total_pagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Deseados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]