# Generated by Django 5.0.6 on 2024-10-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
