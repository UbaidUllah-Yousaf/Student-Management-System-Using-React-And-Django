# Generated by Django 3.1.4 on 2021-02-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_auto_20210209_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=20),
        ),
    ]
