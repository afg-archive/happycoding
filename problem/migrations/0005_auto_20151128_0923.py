# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_auto_20151128_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='code',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
