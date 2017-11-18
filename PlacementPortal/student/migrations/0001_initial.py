# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 20:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_number', models.IntegerField(choices=[(0, 'One page'), (1, 'Two page Tech'), (2, 'One page Nontech'), (3, 'CV')], verbose_name='Resume number')),
                ('file', models.FileField(upload_to='', verbose_name='Resume pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Student ID')),
                ('name', models.CharField(max_length=50, verbose_name='Full name')),
                ('roll_number', models.CharField(max_length=4, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Roll number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number')),
                ('reg_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1958), django.core.validators.MaxValueValidator(2050)], verbose_name='Registration year')),
                ('cpi', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='CPI')),
                ('resume_verified', models.BooleanField(default=False, verbose_name='Resume verified?')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Department', verbose_name='Department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Program', verbose_name='Program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='Resume of'),
        ),
        migrations.AlterUniqueTogether(
            name='resume',
            unique_together=set([('student', 'resume_number')]),
        ),
    ]
