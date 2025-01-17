# Generated by Django 4.2.1 on 2023-12-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StuApp', '0002_com_mst1'),
    ]

    operations = [
        migrations.CreateModel(
            name='com_mst3',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('c1', models.IntegerField()),
                ('c2', models.IntegerField()),
                ('c3', models.IntegerField()),
                ('c4', models.IntegerField()),
                ('total', models.IntegerField(default=0)),
                ('c5', models.IntegerField()),
                ('total1', models.IntegerField(default=0)),
                ('cid', models.ForeignKey(db_column='cid', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.course')),
                ('sid', models.ForeignKey(db_column='sid', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.student')),
                ('type_id', models.ForeignKey(db_column='type_id', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.subject_type')),
            ],
            options={
                'db_table': 'sem4_component_table',
            },
        ),
        migrations.CreateModel(
            name='com_mst2',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('c1', models.IntegerField()),
                ('c2', models.IntegerField()),
                ('c3', models.IntegerField()),
                ('c4', models.IntegerField()),
                ('total', models.IntegerField(default=0)),
                ('c5', models.IntegerField()),
                ('total1', models.IntegerField(default=0)),
                ('cid', models.ForeignKey(db_column='cid', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.course')),
                ('sid', models.ForeignKey(db_column='sid', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.student')),
                ('type_id', models.ForeignKey(db_column='type_id', default='', on_delete=django.db.models.deletion.CASCADE, to='StuApp.subject_type')),
            ],
            options={
                'db_table': 'sem3_component_table',
            },
        ),
    ]
