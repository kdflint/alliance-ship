from apps.shared.models import Backlog, Status, TeamProject
from alliance.core.lib.views_helper import get_object_or_none
from .constants import DB_OPEN_STATUS_NAME, DB_SELECTED_STATUS_NAME,\
    DB_QUEUED_STATUS_NAME, DB_ACCEPTED_STATUS_NAME


def retrieve_backlogs_by_status_project_and_priority(team_id):
    return Backlog.objects.filter(
        project__id__in=project_id_list(team_id),
        status__id__in=status_id_list(),
        priority__in=priority_list())


def status_id_list():
    return [s for s in [open_status_id(), selected_status_id(), queued_status_id()] if s]


def project_id_list(team_id):
    return TeamProject.objects.filter(
        team__id=team_id).values_list('project_id')


def priority_list():
    return ['0', '1', '2']


def open_status_id():
    return status_id(DB_OPEN_STATUS_NAME)


def selected_status_id():
    return status_id(DB_SELECTED_STATUS_NAME)


def queued_status_id():
    return status_id(DB_QUEUED_STATUS_NAME)


def accepted_status_id():
    return status_id(DB_ACCEPTED_STATUS_NAME)


def status_id(name):
    status = get_object_or_none(Status, category='backlog', name=name)
    if status:
        return status.id
    return None
