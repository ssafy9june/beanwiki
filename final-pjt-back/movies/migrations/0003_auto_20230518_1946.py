# Generated by Django 3.2.18 on 2023-05-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230518_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='popularity',
            field=models.FloatField(null=True),
        ),
    ]