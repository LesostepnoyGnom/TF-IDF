# Generated by Django 5.1.7 on 2025-06-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_documents_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
