# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20151128_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='description',
        ),
    ]
