# Generated by Django 4.2.5 on 2023-11-19 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userFolder', '0008_alter_account_status'),
        ('adminpage', '0003_logbook_delete_recordprocesstogetreco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook',
            name='about',
            field=models.CharField(default='logging in', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='getdocuments',
            name='fk_account',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='userFolder.account'),
        ),
    ]
