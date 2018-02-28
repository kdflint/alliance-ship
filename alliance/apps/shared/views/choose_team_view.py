from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from apps.shared.models import Team
from core.lib.shortcuts import create_json_message_object
from apps.shared.forms.choose_team_form import ChooseTeamForm
from apps.shared.views.mixins.requiresigninajax import RequireSignIn
from django.shortcuts import redirect
from apps.backlog.util import (retrieve_backlogs_by_acstatus_project_and_priority, retrieve_backlogs_by_project_status_and_priority)
from apps.shared.models import Estimate
from core.lib.views_helper import get_object_or_none
import logging

class ChooseTeam(RequireSignIn, View):

    def get(self, request):
        logger = logging.getLogger("alliance")
        results = {'success': False}
        team_ids = request.session['test-teams']
        teams = Team.objects.filter(id__in=team_ids).values_list('id', 'name')
        request.session['statusFlag'] = None
        request.session['teamVelocity'] = 0
        request.session['acceptedVelocity'] = 0
        if (len(teams) == 0):
            results['errors'] = create_json_message_object(
                "There is no team associated with this volunteer.")
        elif (len(teams) == 1):
            request.session['team'] = teams[0].id
            results['messages'] = create_json_message_object(
                "Unique team already associated")
        else:
            form = ChooseTeamForm(request)
            results['html'] = render_to_string('core/choose_team.txt',
                                               {'form': form})
            results['success'] = True
        return JsonResponse(results)

    def post(self, request):
        logger = logging.getLogger("alliance")
        results = {'success': False}
        form = ChooseTeamForm(request, request.POST)
        logger.debug("form in post")
        logger.debug(form)
        logger.debug(form.is_valid())
        if form.is_valid():
            team = form.cleaned_data['team']
            request.session['team'] = team
            results['success'] = True
			
            logger.debug(form.fields['team'])
            choiceFieldObj = form.fields['team']
            logger.debug(choiceFieldObj.choices)
            logger.debug("choiceFieldObj choices size : %d ",len(choiceFieldObj.choices))
            teamId = int(team)
            logger.debug("Integer converted team id : %d ", teamId)
			
            i = 0
            while (i < len(choiceFieldObj.choices)):
                if (teamId == choiceFieldObj.choices[i][0]):
                    logger.debug("Match found in index %d for team id %d ", i, choiceFieldObj.choices[i][0])
                    logger.debug(choiceFieldObj.choices[i][1])
                    request.session['team'] = teamId
                    request.session['teamName'] = choiceFieldObj.choices[i][1]
                else:
                   logger.debug("Match Not found in index for %d team id %d", i, choiceFieldObj.choices[i][0])
                i += 1

        else:
            results['errors'] = form.errors.as_json()

        # Team Velocity for Completed backlogs : START
        statusFlag = 'COMPLETE'
        priorityFlag = '9'
        completedBacklogs = retrieve_backlogs_by_project_status_and_priority(teamId, statusFlag, priorityFlag) \
            .order_by('project__name', 'module', 'sprint_id', 'priority', 'id')

        previousRecSprint = 0
        currentRecSprint = 0
        bgCountBySprint = 0
        totalEstimateSum = 0
        estimateValue = 0
        estimateList = []
        myTeamVelocitydict = {}

        for backlog in completedBacklogs:

            estimate = get_object_or_none(Estimate, team_id=teamId, backlog_id=backlog.id)

            if not estimate:
                estimate = Estimate(team_id=teamId, backlog_id=backlog.id)

            currentRecSprint = backlog.sprint_id
            estimateValue = estimate.estimate
            logger.debug(estimate)
            logger.debug(estimateValue)

            if bgCountBySprint == 0:
                previousRecSprint = currentRecSprint

            if currentRecSprint == previousRecSprint:
                bgCountBySprint += 1
                estimateList.append(int(estimateValue))
            else:
                myTeamVelocitydict.update({previousRecSprint: estimateList})
                bgCountBySprint = 1
                estimateList = []
                estimateList.append(int(estimateValue))

            previousRecSprint = currentRecSprint

        myTeamVelocitydict.update({previousRecSprint: estimateList})
        logger.debug(myTeamVelocitydict)

        for key in myTeamVelocitydict:
            logger.debug(key)
            logger.debug(myTeamVelocitydict[key])
            estimateSum = sum(myTeamVelocitydict[key])
            logger.debug(estimateSum)
            totalEstimateSum += estimateSum
            logger.debug(totalEstimateSum)

        logger.debug(len(myTeamVelocitydict.keys()))
        teamVelocity = totalEstimateSum / len(myTeamVelocitydict.keys())
        logger.debug(teamVelocity)

        request.session['teamVelocity'] = teamVelocity
        # Team Velocity for Completed backlogs : END

        # Accepted Velocity for current/recent sprint : START
        statusFlag = 'OPEN'
        priorityFlag = '9'
        backlogs = retrieve_backlogs_by_project_status_and_priority(teamId, statusFlag, priorityFlag) \
            .order_by('project__name', 'module', 'sprint_id', 'priority', 'id')

        acceptedSprint = 0
        acceptedEstimate = 0
        acceptedEstimateVel = 0

        for backlog in backlogs:
            estimate = get_object_or_none(Estimate, team_id=teamId, backlog_id=backlog.id)
            if not estimate:
                estimate = Estimate(team_id=teamId, backlog_id=backlog.id)

            acceptedSprint = backlog.sprint_id
            acceptedEstimate = estimate.estimate
            logger.debug(estimate)
            logger.debug(acceptedEstimate)

            if acceptedSprint != None and acceptedEstimate != None:
                acceptedEstimateVel += int(acceptedEstimate)

            request.session['acceptedVelocity'] = acceptedEstimateVel
            logger.debug(acceptedEstimateVel)
        # Accepted Velocity for current/recent sprint : END
        return JsonResponse(results)
