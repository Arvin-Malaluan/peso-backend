# Generated by Django 4.2.5 on 2023-11-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0039_alter_allprofile_emp_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allprofile',
            name='emp_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='subsidiaries_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
