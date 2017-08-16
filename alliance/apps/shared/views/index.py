from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from apps.shared.models import Team
from apps.shared.forms.choose_team_form import ChooseTeamForm
import logging

@login_required
def index(request):
	
    teamString = ''
    teamRaw = ''
    teams = []
    logger = logging.getLogger("alliance")

    if request.method == 'POST':
        form = ChooseTeamForm(request, request.POST or None)
        if form.is_valid():
            team = form.cleaned_data['team']
            request.session['team'] = team
    else:
        team = request.session.get('team')

    if team is None:
        teams = []
        teams2 = []
        # The python_social_auth authentication pipeline puts the github user teams on the session
        # Here, we match those teams to ones recognized in our system and present a selection dropdown if > 1
        logger.debug("These github teams are on the session: " + request.session['gh_teams'])
        if request.session['gh_teams'] == "unauthorized":
					return render(request, 'accounts/logged.html')	       	
        gh_team_raw = request.session['gh_teams']	
        gh_team_chopped = gh_team_raw.rpartition(',')[0]
        gh_team_names = gh_team_chopped.split(",")
        for item in gh_team_names:
        	logger.debug("matching on " + item)
        	team_qs = Team.objects.filter(name=item)
        	if team_qs:
        		teams.append(team_qs[0])
        		teams2.append(team_qs[0].id)
        logger.debug("We matched %d system teams in the view", len(teams))
        logger.debug(teams)
        logger.debug(teams2)
        if (len(teams) == 0):
            request.session['team'] = None
            request.session['teamName'] = None
        elif (len(teams) == 1):
            request.session['team'] = teams[0].id
            request.session['teamName'] = teams[0].name
            return redirect('/alliance/apps/backlog/')
        else:
            request.session['test-teams'] = teams2
            request.session['teamName'] = None
            request.session['multiTeams'] = "True"
            form = ChooseTeamForm(request)
            context = RequestContext(request, {'teams': teams,
                                               'form': form})
            return render(request, 'core/index.html', context)

    return render(request, 'core/index.html')
