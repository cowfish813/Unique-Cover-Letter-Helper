# Generated by Django 3.1 on 2020-09-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0029_auto_20200909_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_posting_website',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
