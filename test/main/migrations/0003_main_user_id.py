# Generated by Django 5.1.7 on 2025-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
