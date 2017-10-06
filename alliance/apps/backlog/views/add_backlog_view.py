from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from apps.shared.models import Backlog
from apps.shared.views.mixins.requiresigninajax import RequireSignIn
from ...backlog.forms import BacklogNewForm
import logging

class BacklogFormView(RequireSignIn, CreateView):
    model = Backlog
    form_class = BacklogNewForm

    def get(self, request):
        logger = logging.getLogger("alliance")
        logger.debug("Inside BacklogFormView GET >>>>>>>>>>>>>>>>>>>")
        results = {'success': False}

        # Get the volunteers team
        team_id = request.session.get('team')

        # Redirects to the index page if there is no team associated
        if team_id is None:
            return redirect(reverse('index'))

        form = BacklogNewForm(request.GET)
        logger.debug("Backlog Get FORM")
        return render(request, 'backlog/backlog_form.html', {'form' : form})

    def post(self, request):
        logger = logging.getLogger("alliance")
        logger.debug("Inside BacklogFormView POST >>>>>>>>>>>>>>>>>>>")
        logger.debug(request.POST)
        results = {'success': False}
        results['errors'] = None
        logger.debug(results)

        # Get the volunteers team
        team_id = request.session.get('team')

        # Redirects to the index page if there is no team associated
        if team_id is None:
            return redirect(reverse('index'))

        form = BacklogNewForm(request.POST)
        if form.is_valid():
            logger.debug("Inside is valid")
            logger.debug(form.cleaned_data['story_title'])
            logger.debug(form.cleaned_data['story_descr'])
            logger.debug(form.cleaned_data['priority'])

            results = form.save(request, commit=True)
            logger.debug(results)
            logger.debug(results['success'])
            logger.debug(results['errors'])

            if results['errors'] is None:
                logger.debug("No errors!")
                return redirect('backlogs')
        elif "Cancel" in request.POST.get("action-cancel"):
            logger.debug("Matching request.POST !!!!!")
            return redirect('backlogs')
        else: 
            results['errors'] = form.errors.as_json()

        return render(request, 'backlog/backlog_form.html', {'obj_as_json' : results})
