# Generated by Django 2.2 on 2019-07-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energyaudit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='name',
            field=models.CharField(choices=[('fridge', 'Fridge'), ('air conditioner', 'Air Conditioner'), ('washing machine', 'Washing Machine')], max_length=60, verbose_name='Appliance'),
        ),
    ]
