from django import forms
from ..models import Team

class ChooseTeamForm(forms.Form):
    team = forms.ChoiceField(choices=[], widget=forms.Select(),
                             required=True, label='Choose a Team')

    def __init__(self, request, *args, **kwargs):
        super(ChooseTeamForm, self).__init__(*args, **kwargs)      
        team_ids = request.session['test-teams']
        self.fields['team'].choices = Team.objects.filter(id__in=team_ids).values_list('id', 'name')


