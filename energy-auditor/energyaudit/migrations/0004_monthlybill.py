# Generated by Django 2.2 on 2019-07-18 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('energyaudit', '0003_auto_20190718_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.DateField()),
                ('bill_amount', models.IntegerField()),
                ('power_consumed', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
