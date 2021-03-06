# Generated by Django 3.2.8 on 2021-10-20 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('sportname', models.CharField(max_length=30)),
                ('sportdesc', models.CharField(blank=True, max_length=600, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('teamname', models.CharField(max_length=30)),
                ('teamdesc', models.CharField(blank=True, max_length=600, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.sport')),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('playername', models.CharField(max_length=50)),
                ('playerdesc', models.CharField(max_length=300)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.sport')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.team')),
            ],
        ),
        migrations.CreateModel(
            name='match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchdesc', models.CharField(max_length=800)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('matchtype', models.CharField(blank=True, max_length=40, null=True)),
                ('venue', models.CharField(blank=True, max_length=50, null=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.sport')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='structure.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='structure.team')),
            ],
        ),
    ]
