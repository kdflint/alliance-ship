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
    if request.method == 'POST':
        form = ChooseTeamForm(request, request.POST or None)
        if form.is_valid():
            team = form.cleaned_data['team']
            request.session['team'] = team
    else:
        team = request.session.get('team')

    if team is None:
        logger = logging.getLogger("alliance")
        #user_email = request.user.email
        #teams = Team.objects.filter(volunteers__email=user_email)
        teamRaw = request.user.first_name + request.user.last_name
        #logger.debug("Team raw = " + teamRaw)
        teamFilterString = teamRaw.rpartition(',')[0]
        logger.debug(teamFilterString)
        # TODO - craft  teamFilterString such that it will work in query
        # OR split the string into a list and iterate, using get action for the filter
        teams = Team.objects.filter(name__in = [teamFilterString])
        #teams = Team.objects.filter(name__in = ['2015 Summer Interns','Developer','North Stars','Owners'])
        #teams = Team.objects.all()
        logger.debug(len(teams))
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
