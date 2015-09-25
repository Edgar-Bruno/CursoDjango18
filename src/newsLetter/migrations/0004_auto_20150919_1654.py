# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetter', '0003_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='aniversario',
            new_name='Aniversario',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='Usuario',
        ),
    ]
