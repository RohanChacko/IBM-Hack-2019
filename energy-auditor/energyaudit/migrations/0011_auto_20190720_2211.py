# Generated by Django 2.2 on 2019-07-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energyaudit', '0010_auto_20190720_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='house_type',
            field=models.CharField(choices=[('apartment', 'Apartment'), ('villa', 'Villa'), ('bungalow', 'Bungalow')], default='Apartment', max_length=60, verbose_name='House Type'),
        ),
    ]
