# Generated by Django 4.2.5 on 2023-11-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_loguserengagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_count', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='RecordProcessToGetReco',
        ),
        migrations.DeleteModel(
            name='TimeToGetCompatibilityScore',
        ),
    ]
