# Generated by Django 4.1.7 on 2023-05-19 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProyecto', '0003_conexion_led'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesion_terapia',
            fields=[
                ('Id_sesion', models.IntegerField(primary_key=True, serialize=False)),
                ('Id_emocion', models.IntegerField()),
                ('fecha_sesi', models.DateField()),
                ('nivel_satif', models.IntegerField()),
                ('Id_conexion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appProyecto.conexion_led')),
                ('Id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appProyecto.usuario')),
            ],
        ),
    ]
