# Generated by Django 3.2.8 on 2021-10-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_alter_player_inmatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(blank=True, default='batsman', max_length=20, null=True),
        ),
    ]
