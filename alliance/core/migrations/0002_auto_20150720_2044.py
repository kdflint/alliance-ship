# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptanceCriteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descr', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=80, null=True)),
            ],
            options={
                'db_table': 'acceptance_criteria',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(default=b'NULL', max_length=200, null=True)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(default=b'NULL', max_length=100)),
                ('amount_goal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('respondent_goal', models.CharField(default=b'NULL', max_length=10)),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_id', models.IntegerField(db_column=b'team_id_fk')),
                ('backlog_id', models.IntegerField(db_column=b'backlog_id_fk')),
                ('estimate', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'estimate',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=120, null=True)),
                ('descr', models.CharField(default=b'NULL', max_length=1000, null=True)),
                ('application', models.ForeignKey(to='core.Application', db_column=b'application_id_fk')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=25, null=True)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='TeamProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('claim_backlog', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'team_project',
            },
        ),
        migrations.CreateModel(
            name='TeamVolunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'Follower', max_length=20)),
                ('conference_link', models.CharField(default=b'NULL', max_length=120)),
            ],
            options={
                'db_table': 'team_volunteer',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(default=b'NULL', max_length=255)),
                ('fname', models.CharField(default=b'NULL', max_length=50)),
                ('lname', models.CharField(max_length=50, null=True)),
                ('status_depr', models.CharField(max_length=10, null=True)),
                ('create_dttm', models.DateTimeField(default=datetime.datetime.now)),
                ('update_dttm', models.DateTimeField(null=True)),
                ('descr', models.CharField(max_length=1000)),
                ('campaign', models.ForeignKey(to='core.Campaign', db_column=b'campaign_id_fk')),
            ],
            options={
                'db_table': 'volunteer',
            },
        ),
        migrations.RemoveField(
            model_name='acceptance_criteria',
            name='backlog',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='project_id_fk',
        ),
        migrations.RemoveField(
            model_name='event',
            name='schedule_id_fk',
        ),
        migrations.AddField(
            model_name='backlog',
            name='create_dttm',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='backlog',
            name='update_dttm',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterModelTable(
            name='backlog',
            table='backlog',
        ),
        migrations.AlterModelTable(
            name='event',
            table='event',
        ),
        migrations.AlterModelTable(
            name='status',
            table='status',
        ),
        migrations.AlterModelTable(
            name='team',
            table='team',
        ),
        migrations.DeleteModel(
            name='Acceptance_criteria',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='status',
            field=models.ForeignKey(to='core.Status', db_column=b'status_id_fk'),
        ),
        migrations.AddField(
            model_name='teamvolunteer',
            name='team',
            field=models.ForeignKey(to='core.Team', db_column=b'team_id_fk'),
        ),
        migrations.AddField(
            model_name='teamvolunteer',
            name='volunteer',
            field=models.ForeignKey(to='core.Volunteer', db_column=b'volunteer_id_fk'),
        ),
        migrations.AddField(
            model_name='teamproject',
            name='end_event',
            field=models.ForeignKey(related_name='end_event', db_column=b'end_event_fk', to='core.Event'),
        ),
        migrations.AddField(
            model_name='teamproject',
            name='project',
            field=models.ForeignKey(to='core.Project', db_column=b'project_id_fk'),
        ),
        migrations.AddField(
            model_name='teamproject',
            name='start_event',
            field=models.ForeignKey(related_name='start_event', db_column=b'start_event_fk', to='core.Event'),
        ),
        migrations.AddField(
            model_name='teamproject',
            name='team',
            field=models.ForeignKey(to='core.Team', db_column=b'team_id_fk'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_event',
            field=models.ForeignKey(related_name='end', db_column=b'end_event_fk', to='core.Event'),
        ),
        migrations.AddField(
            model_name='project',
            name='schedule',
            field=models.ForeignKey(to='core.Schedule', db_column=b'schedule_id_fk'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_event',
            field=models.ForeignKey(related_name='start', db_column=b'start_event_fk', to='core.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='estimate',
            unique_together=set([('team_id', 'backlog_id')]),
        ),
        migrations.AddField(
            model_name='acceptancecriteria',
            name='backlog',
            field=models.ForeignKey(to='core.Backlog', db_column=b'backlog_id_fk'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='project',
            field=models.ForeignKey(db_column=b'project_id_fk', default=139, to='core.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.ForeignKey(db_column=b'schedule_id_fk', default=139, to='core.Schedule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='volunteers',
            field=models.ManyToManyField(to='core.Volunteer', through='core.TeamVolunteer'),
        ),
        migrations.AlterUniqueTogether(
            name='teamvolunteer',
            unique_together=set([('volunteer', 'team')]),
        ),
    ]
