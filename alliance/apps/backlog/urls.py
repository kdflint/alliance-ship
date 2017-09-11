from django.conf.urls import url
from .views import BacklogView, BacklogFormView, GitHubWebhookView, CheckBacklogsView

urlpatterns = [
    url(r'^$', BacklogView.as_view(), name='backlogs'),
	url(r'^add$', BacklogFormView.as_view(), name='backlogsForm'),
    url(r'^checkBacklogs$', CheckBacklogsView.as_view(),
        name='checkBacklogsUpdate'),
    url(r'^githubimport$', GitHubWebhookView.as_view(), name='ghWebhook'),
]
