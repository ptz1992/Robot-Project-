# Generated by Django 4.1.5 on 2023-01-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omorobot', '0009_auto_20230119_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicar',
            name='battery',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='minicar',
            name='speed',
            field=models.IntegerField(default=0),
        ),
    ]
