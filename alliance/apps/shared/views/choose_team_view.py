from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from apps.shared.models import Team
from core.lib.shortcuts import create_json_message_object
from apps.shared.forms.choose_team_form import ChooseTeamForm
from apps.shared.views.mixins.requiresigninajax import RequireSignIn
from django.shortcuts import redirect
import logging

class ChooseTeam(RequireSignIn, View):

    def get(self, request):
        logger = logging.getLogger("alliance")
        results = {'success': False}
        team_ids = request.session['test-teams']
        teams = Team.objects.filter(id__in=team_ids).values_list('id', 'name')
        request.session['statusFlag'] = None
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
        return JsonResponse(results)
