# Generated by Django 3.1.4 on 2023-01-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omorobot', '0008_remove_minicar_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
