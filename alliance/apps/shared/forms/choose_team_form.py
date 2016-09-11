from django import forms
from ..models import Team

class ChooseTeamForm(forms.Form):
    team = forms.ChoiceField(choices=[], widget=forms.Select(),
                             required=True, label='Choose a Team')

    def __init__(self, request, teams, *args, **kwargs):
        super(ChooseTeamForm, self).__init__(*args, **kwargs)      
        team_id = []
        for item in teams:
            team_id.append(item.id)
        self.fields['team'].choices = Team.objects.filter(id__in=team_id).values_list('id', 'name')


