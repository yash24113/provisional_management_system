# Generated by Django 4.2.1 on 2023-12-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StuApp', '0003_com_mst3_com_mst2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_result',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
