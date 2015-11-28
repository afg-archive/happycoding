# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oj_id', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='hint',
            name='problem',
            field=models.ForeignKey(to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='hint',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='code',
            name='problem',
            field=models.ForeignKey(to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='code',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
