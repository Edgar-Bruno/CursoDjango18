# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='mensagem',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
