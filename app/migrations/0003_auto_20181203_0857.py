# Generated by Django 2.0.5 on 2018-12-03 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_conferenceattendants_attendants_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conferencefeedback',
            options={'verbose_name': 'Conference Feedback', 'verbose_name_plural': 'Conference Feedback'},
        ),
    ]
