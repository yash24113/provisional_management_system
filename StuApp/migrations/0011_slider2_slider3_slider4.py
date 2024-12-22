# Generated by Django 4.2.1 on 2023-12-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StuApp', '0010_alter_slider1_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_Main_Img', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 'slider2',
            },
        ),
        migrations.CreateModel(
            name='slider3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_Main_Img', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 'slider3',
            },
        ),
        migrations.CreateModel(
            name='slider4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_Main_Img', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 'slider4',
            },
        ),
    ]