# Generated by Django 3.0.3 on 2020-08-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0004_auto_20200818_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('street_address', models.CharField(blank=True, max_length=200)),
                ('city_address', models.CharField(blank=True, max_length=200)),
                ('state_address', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='CoverLetter',
        ),
    ]
