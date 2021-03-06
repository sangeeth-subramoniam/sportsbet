# Generated by Django 3.2.8 on 2021-10-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('teamname', 'sport')},
        ),
    ]
