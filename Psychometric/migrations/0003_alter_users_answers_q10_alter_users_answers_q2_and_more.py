# Generated by Django 5.1.1 on 2024-10-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Psychometric', '0002_users_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_answers',
            name='q10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users_answers',
            name='q9',
            field=models.CharField(max_length=10, null=True),
        ),
    ]