# Generated by Django 2.0.2 on 2018-03-02 02:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0005_auto_20180220_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
