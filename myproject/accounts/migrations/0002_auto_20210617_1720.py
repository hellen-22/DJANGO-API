# Generated by Django 3.0.6 on 2021-06-17 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='user',
        ),
    ]