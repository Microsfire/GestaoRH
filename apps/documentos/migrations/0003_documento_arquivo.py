# Generated by Django 3.2.1 on 2021-05-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_alter_documento_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default='', upload_to='documentos'),
            preserve_default=False,
        ),
    ]
