# Generated by Django 4.1.5 on 2023-01-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("omorobot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mycar",
            name="check_time",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="mycar",
            name="mycar_encoder_ac",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="mycar",
            name="mycar_encoder_or",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="mycar",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_password",
            field=models.CharField(max_length=20, null=True),
        ),
    ]