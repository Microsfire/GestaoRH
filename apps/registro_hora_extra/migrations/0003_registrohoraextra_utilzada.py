# Generated by Django 3.2.3 on 2021-07-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilzada',
            field=models.BooleanField(default=False),
        ),
    ]
