# Generated by Django 4.0.4 on 2022-05-27 18:21

from django.db import migrations, models
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_alter_problem_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='scan',
            field=models.FileField(blank=True, default=None, null=True, upload_to=exams.models.folder_name2),
        ),
        migrations.AlterField(
            model_name='result',
            name='scan',
            field=models.FileField(default=None, upload_to=exams.models.folder_name),
        ),
    ]
