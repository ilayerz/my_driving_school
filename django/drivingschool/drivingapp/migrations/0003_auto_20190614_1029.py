# Generated by Django 3.0 on 2019-06-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivingapp', '0002_auto_20190614_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.DateField(),
        ),
    ]
