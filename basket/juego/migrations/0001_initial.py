# Generated by Django 2.2.dev20180521165340 on 2018-05-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apodo', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
                ('rut', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('estatura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('poscicion', models.CharField(max_length=50)),
            ],
        ),
    ]
