# Generated by Django 4.2 on 2024-05-09 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lloguer', '0002_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='atuo',
            new_name='auto',
        ),
    ]
