# Generated by Django 5.1.1 on 2024-11-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_emotion_analysis_emotion_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion_analysis',
            name='emotion_type',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
