# Generated by Django 5.0.6 on 2024-10-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_details_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='address',
            field=models.CharField(max_length=225),
        ),
    ]
