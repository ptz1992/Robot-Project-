# Generated by Django 4.1.5 on 2023-01-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omorobot', '0012_alter_minicar_battery_alter_minicar_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicar',
            name='battery',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='minicar',
            name='speed',
            field=models.IntegerField(null=True),
        ),
    ]