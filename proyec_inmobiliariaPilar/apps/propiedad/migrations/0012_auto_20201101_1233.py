# Generated by Django 3.1.2 on 2020-11-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0011_auto_20201031_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='capacidad_cochera',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
