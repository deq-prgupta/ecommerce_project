# Generated by Django 3.2 on 2022-07-20 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20220720_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today, verbose_name='DOB'),
        ),
    ]
