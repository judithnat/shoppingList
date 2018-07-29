# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoplistclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('shop', models.CharField(choices=[('SM', 'supermarket'), ('BL', 'bramcotelane'), ('TN', 'town'), ('OS', 'other_shop')], default='SM', max_length=20)),
                ('category', models.CharField(choices=[('FD', 'food'), ('CL', 'cleaning'), ('PH', 'pharmacy'), ('CT', 'clothes'), ('OC', 'other_category')], default='FD', max_length=20)),
                ('quantity', models.IntegerField(max_length=5)),
                ('entered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('urgency', models.CharField(choices=[('UG', 'urgent'), ('SN', 'soon'), ('LU', 'lessurgent'), ('ST', 'sometime')], default='SN', max_length=20)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
