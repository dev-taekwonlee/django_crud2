# Generated by Django 4.0.5 on 2022-06-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
