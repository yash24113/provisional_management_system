# Generated by Django 4.2.1 on 2023-12-09 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StuApp', '0007_alter_student_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sem_id',
        ),
        migrations.AddField(
            model_name='student',
            name='did',
            field=models.ForeignKey(db_column='did', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.department'),
        ),
    ]
