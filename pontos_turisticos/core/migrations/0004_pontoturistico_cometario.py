# Generated by Django 2.1.5 on 2019-01-13 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='cometario',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
