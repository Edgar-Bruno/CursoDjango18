# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetter', '0004_auto_20150919_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mensagem',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
