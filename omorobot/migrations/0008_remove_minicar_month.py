# Generated by Django 3.1.4 on 2023-01-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omorobot', '0007_auto_20230119_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minicar',
            name='month',
        ),
    ]
