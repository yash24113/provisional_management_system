# Generated by Django 4.2.1 on 2023-09-27 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='name',
        ),
    ]
