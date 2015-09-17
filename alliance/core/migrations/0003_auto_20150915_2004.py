# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150720_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='descr',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='backlog',
            name='project',
            field=models.ForeignKey(db_column=b'project_id_fk', to='core.Project', null=True),
        ),
        migrations.AlterField(
            model_name='backlog',
            name='sprint',
            field=models.ForeignKey(db_column=b'sprint_id_fk', to='core.Event', null=True),
        ),
        migrations.AlterField(
            model_name='backlog',
            name='team',
            field=models.ForeignKey(db_column=b'team_id_fk', to='core.Team', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='schedule',
            field=models.ForeignKey(db_column=b'schedule_id_fk', to='core.Schedule', null=b'True'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='create_dttm',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status_depr',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='update_dttm',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='status',
            unique_together=set([('category', 'name')]),
        ),
    ]
