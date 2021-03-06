# Generated by Django 3.0.3 on 2020-08-17 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('top_skills', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extra_line_one', models.TextField(blank=True, null=True)),
                ('bullet_point_two', models.TextField(blank=True, null=True)),
                ('bullet_point_three', models.TextField(blank=True, null=True)),
                ('bullet_point_four', models.TextField(blank=True, null=True)),
                ('bullet_point_five', models.TextField(blank=True, null=True)),
                ('bullet_point_six', models.TextField(blank=True, null=True)),
                ('bullet_point_seven', models.TextField(blank=True, null=True)),
                ('bullet_point_eight', models.TextField(blank=True, null=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter_title', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('job_title', models.CharField(max_length=200)),
                ('cover_letter', models.TextField()),
                ('job_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coverLetters.Job')),
            ],
        ),
    ]
