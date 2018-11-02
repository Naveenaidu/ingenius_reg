# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0010_auto_20181102_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
