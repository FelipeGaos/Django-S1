# Generated by Django 2.2.dev20180521165340 on 2018-05-23 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_auto_20180523_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juego.equipo'),
        ),
    ]
