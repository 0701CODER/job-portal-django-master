# Generated by Django 3.2.7 on 2023-12-07 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_alter_job_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 7, 9, 43, 21, 32056)),
        ),
    ]
