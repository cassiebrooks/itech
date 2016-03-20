# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quokka', '0004_auto_20160309_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.ForeignKey(default=1, to='quokka.Set'),
            preserve_default=False,
        ),
    ]
