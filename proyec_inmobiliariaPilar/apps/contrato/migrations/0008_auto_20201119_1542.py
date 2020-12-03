# Generated by Django 3.1.2 on 2020-11-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0007_auto_20201118_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilinopropiedad',
            name='cancelacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inquilinopropiedad',
            name='fecha_cancelacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propietariopropiedad',
            name='cancelacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='propietariopropiedad',
            name='fecha_cancelacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
