from django.shortcuts import render
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
        #teams = Team.objects.filter(volunteers__email=user_email)
        # This is hacksville!!
        # First, the pipeline is using the user details string fields to communicate with this view. See pipeline.py. 
        # Second, the user should be redirected before here, preferably in the pipeline.
        if request.user.first_name == "unauthorized":
					logger.info("No membership teams matched with Northbridge Organization for user " + request.user.username)
					return render(request, 'accounts/logged.html')	       	
        teamRaw = request.user.first_name + request.user.last_name	
        teamChopped = teamRaw.rpartition(',')[0]
        teamNames = teamChopped.split(",");
        for item in teamNames:
        	_team = Team.objects.filter(name = item)
        	if _team:
        		teams.append(_team)
        logger.debug("We found some teams")
        logger.debug(teams)
        if (len(teams) == 0):
            request.session['team'] = None
        elif (len(teams) == 1):
            request.session['team'] = teams[0].id
        else:
            form = ChooseTeamForm(request)
            context = RequestContext(request, {'teams': teams,
                                               'form': form})
            return render(request, 'core/index.html', context)

    return render(request, 'core/index.html')
