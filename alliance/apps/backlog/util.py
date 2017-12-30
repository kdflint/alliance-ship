from apps.shared.models import Backlog, Status, TeamProject
from core.lib.views_helper import get_object_or_none
from .constants import DB_OPEN_STATUS_NAME, DB_SELECTED_STATUS_NAME,\
    DB_QUEUED_STATUS_NAME, DB_ACCEPTED_STATUS_NAME
import logging

def retrieve_backlogs_by_status_project_and_priority(team_id):
    return Backlog.objects.filter(
        project__id__in=project_id_list(team_id),
        status__id__in=status_id_list(),
        priority__in=priority_list())

def retrieve_backlogs_by_acstatus_project_and_priority(team_id):
    return Backlog.objects.filter(
        project__id__in=project_id_list(team_id),
        status__id__in=acstatus_id_list(),
        priority__in=priority_list())

def retrieve_backlogs_by_project_status_and_priority(team_id, statusFlag, priorityFlag):
    logger = logging.getLogger("alliance")
    logger.debug("Inside retrieve_backlogs_by_project_status_and_priority")
    logger.debug(team_id)
    logger.debug(statusFlag)
    logger.debug(priorityFlag)
	
    status_list=[]
    if (statusFlag == 'COMPLETE'):
        status_list=acstatus_id_list()
    else:
        status_list=status_id_list()

    priority_lists=[]
    if (priorityFlag == '3'):
        priority_lists=['0', '1', '2','3']
    elif (priorityFlag == '4'):
        priority_lists=['0', '1', '2','3','4']
    elif (priorityFlag == '5'):
        priority_lists=['0', '1', '2','3','4','5']
    elif (priorityFlag == '6'):
        priority_lists=['0', '1', '2','3','4','5','6']
    elif (priorityFlag == '7'):
        priority_lists=['0', '1', '2','3','4','5','6','7']
    elif (priorityFlag == '8'):
        priority_lists=['0', '1', '2','3','4','5','6','7','8']
    elif (priorityFlag == '9'):
        priority_lists=['0', '1', '2','3','4','5','6','7','8','9']
    else:
        priority_lists=priority_list()

    logger.debug(status_list)
    logger.debug(priority_lists)

    return Backlog.objects.filter(
        project__id__in=project_id_list(team_id),
        status__id__in=status_list,
        priority__in=priority_lists)

def status_id_list():
    return [s for s in [open_status_id(), selected_status_id(), queued_status_id()] if s]

def acstatus_id_list():
    return [s for s in [accepted_status_id()] if s]

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
