# Generated by Django 3.2.8 on 2021-10-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportinfo',
            name='sport_desc',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]