# Generated by Django 4.2.5 on 2023-11-15 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_usurio_delete_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usurio',
            new_name='Usuario',
        ),
    ]
