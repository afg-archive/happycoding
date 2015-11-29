# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0005_auto_20151128_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='HintUpvote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='hint',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hintupvote',
            name='hint',
            field=models.ForeignKey(to='problem.Hint'),
        ),
        migrations.AddField(
            model_name='hintupvote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='hintupvote',
            unique_together=set([('user', 'hint')]),
        ),
    ]
