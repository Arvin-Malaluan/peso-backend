# Generated by Django 4.2.5 on 2023-09-24 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userFolder', '0005_alter_account_email_alter_account_role'),
        ('seekerFolder', '0011_remove_comments_account_comments_commentor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='account',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='userFolder.account'),
            preserve_default=False,
        ),
    ]