# Generated by Django 4.2.5 on 2023-10-15 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0009_alter_applicants_applicant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobpost', to='recruiter.jobpost'),
        ),
    ]
