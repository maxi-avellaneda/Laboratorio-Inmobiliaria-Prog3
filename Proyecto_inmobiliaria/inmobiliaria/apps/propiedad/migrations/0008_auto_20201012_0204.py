# Generated by Django 3.0 on 2020-10-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0007_auto_20201009_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='descrip_prop',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='id',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='tipo_propiedad',
        ),
        migrations.RemoveField(
            model_name='propiedadoferta',
            name='id',
        ),
        migrations.AddField(
            model_name='propiedadcasa',
            name='tipo_propiedad',
            field=models.CharField(default='casa', max_length=5),
        ),
        migrations.AddField(
            model_name='propiedaddepto',
            name='tipo_propiedad',
            field=models.CharField(default='departamento', max_length=12),
        ),
        migrations.AddField(
            model_name='propiedadhabitacion',
            name='tipo_propiedad',
            field=models.CharField(default='habitacion', max_length=10),
        ),
        migrations.AlterField(
            model_name='inquilinopropiedad',
            name='importe_senia',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='inquilinopropiedad',
            name='importe_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='cod_propiedad',
            field=models.DecimalField(decimal_places=0, max_digits=6, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='propiedadoferta',
            name='cod_oferta',
            field=models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False, unique=True),
        ),
    ]
