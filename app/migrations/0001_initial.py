# Generated by Django 4.1 on 2022-11-23 08:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('segundo_nombre', models.CharField(max_length=40, null=True)),
                ('segundo_apellido', models.CharField(max_length=40, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('subTotal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('segundo_nombre', models.CharField(max_length=40, null=True)),
                ('segundo_apellido', models.CharField(max_length=40, null=True)),
                ('direccion', models.CharField(max_length=128)),
                ('barrio', models.CharField(max_length=64)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('imagen', models.ImageField(upload_to='productos')),
                ('logo', models.ImageField(null=True, upload_to='productos')),
                ('popularidad', models.IntegerField(default=0)),
                ('estrellas', models.IntegerField(default=0)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precioAnterior', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('unidades', models.IntegerField(default=0)),
                ('nuevo', models.BooleanField(default=False)),
                ('descuento', models.BooleanField(default=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='productos')),
                ('popularidad', models.IntegerField(default=0)),
                ('idRestaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detallerOrden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detalleorden')),
                ('estadoOrden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadoorden')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.restaurante')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto'),
        ),
    ]
