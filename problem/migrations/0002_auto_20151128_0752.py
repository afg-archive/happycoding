# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
