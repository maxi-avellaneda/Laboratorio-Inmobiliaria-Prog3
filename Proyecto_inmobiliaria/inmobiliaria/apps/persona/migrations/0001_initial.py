# Generated by Django 3.0 on 2020-10-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_persona', models.DecimalField(decimal_places=1, max_digits=2, unique=True)),
                ('tipo_persona', models.CharField(choices=[('fisica', 'F'), ('juridica', 'J')], max_length=8)),
                ('provincia', models.CharField(max_length=20)),
                ('localidad', models.CharField(max_length=20)),
                ('barrio', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=5)),
                ('telefono', models.CharField(max_length=13)),
                ('mail', models.CharField(max_length=40)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaJuridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=11, unique=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=50)),
                ('cuil', models.CharField(max_length=11, unique=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
        ),
    ]
