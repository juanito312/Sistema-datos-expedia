# Generated by Django 4.2.6 on 2023-11-27 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_usuario_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
