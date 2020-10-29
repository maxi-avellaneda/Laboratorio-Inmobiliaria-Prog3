# Generated by Django 3.1.2 on 2020-10-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0004_auto_20201028_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedadcasa',
            name='tipo_propiedad',
        ),
        migrations.RemoveField(
            model_name='propiedaddepto',
            name='tipo_propiedad',
        ),
        migrations.RemoveField(
            model_name='propiedadhabitacion',
            name='tipo_propiedad',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.CharField(default='default', editable=False, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(default='', upload_to='propiedad'),
            preserve_default=False,
        ),
    ]
