# Generated by Django 5.0.7 on 2024-07-27 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='name',
            new_name='field',
        ),
        migrations.AddField(
            model_name='resume',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='job_title',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=60, null=True)),
                ('company_name', models.CharField(max_length=60, null=True)),
                ('Resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_resume.resume')),
            ],
        ),
    ]
