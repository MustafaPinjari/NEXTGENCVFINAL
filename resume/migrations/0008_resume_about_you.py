# Generated by Django 5.0.6 on 2024-11-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_resume_city_resume_country_resume_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='about_you',
            field=models.TextField(blank=True, null=True),
        ),
    ]
