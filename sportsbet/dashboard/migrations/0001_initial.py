# Generated by Django 3.2.8 on 2021-10-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sportinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(blank=True, max_length=30)),
                ('sport_desc', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
