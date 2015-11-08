from django.db import models
from datetime import datetime
from . import Project, Event, Status, Team


class Backlog(models.Model):
    project = models.ForeignKey(Project, db_column='project_id_fk', null=True, blank=True)
    sprint = models.ForeignKey(Event, db_column='sprint_id_fk', null=True, blank=True)
    story_title = models.CharField(max_length=50)
    story_descr = models.CharField(max_length=2000, null=True, blank=True)
    priority = models.CharField(max_length=1, null=True, default='9', blank=True)
    status = models.ForeignKey(Status, db_column='status_id_fk')
    module = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=2000, null=True, blank=True)
    team = models.ForeignKey(Team, db_column='team_id_fk', null=True, blank=True)
    github_number = models.CharField(max_length=5, null=True, blank=True)
    github_repo = models.CharField(max_length=50, null=True, blank=True)
    create_dttm = models.DateTimeField(default=datetime.now, blank=False)
    update_dttm = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.story_title

    class Meta:
        db_table = "backlog"
