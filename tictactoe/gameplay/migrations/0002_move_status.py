# Generated by Django 2.0.1 on 2018-01-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='status',
            field=models.CharField(default='F', max_length=1),
        ),
    ]
