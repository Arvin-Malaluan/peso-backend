# Generated by Django 4.2.5 on 2023-10-10 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0022_remove_allprofile_id_alter_allprofile_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='poster',
        ),
    ]