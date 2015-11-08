from django.conf.urls import url

from apps.shared.views import ChooseTeam, index

urlpatterns = [
    url(r'^chooseTeam$', ChooseTeam.as_view(), name='chooseTeam'),
    url(r'^index$', index, name='index')
]
