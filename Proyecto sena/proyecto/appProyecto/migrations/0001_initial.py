# Generated by Django 4.1.7 on 2023-05-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Id_usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('contraseña', models.CharField(max_length=15)),
                ('fechaN', models.CharField(max_length=10)),
                ('codigoVer', models.CharField(max_length=10)),
                ('img_perfil', models.CharField(max_length=255)),
                ('estado_cu', models.CharField(max_length=255)),
            ],
        ),
    ]
