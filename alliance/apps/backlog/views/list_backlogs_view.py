from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import JsonResponse
from django.views.generic import View
from django.utils.timezone import localtime
from ..github.export_to import export_to_github
from ..util import (open_status_id, selected_status_id, queued_status_id,
                    retrieve_backlogs_by_status_project_and_priority, 
                    retrieve_backlogs_by_acstatus_project_and_priority, retrieve_backlogs_by_project_status_and_priority)
from apps.shared.models import Backlog, Estimate, Event, Status, Team
from core.lib.shortcuts import create_json_message_object
from apps.shared.views.mixins.requiresigninajax import RequireSignIn
from core.lib.views_helper import get_object_or_none
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging


class BacklogView(RequireSignIn, View):

    def get(self, request):
        logger = logging.getLogger("alliance")
        # Get the volunteers team
        team_id = request.session.get('team')
        # Redirects to the index page if there is no team associated
        if team_id is None:
            return redirect(reverse('index'))

        logger.debug(request.GET)
        results = {'success': False}
        statusResults = False
        statusFlag = request.session.get('statusFlag')
        if 'backlogStatus' in request.GET:
            logger.debug("Inside list_backlog_view backlogStatus")
            request.session['statusFlag'] = None

            if "COMPLETE" in request.GET.getlist("backlogStatus"):
                request.session['statusFlag'] = 'COMPLETE'
            else:
                request.session['statusFlag'] = 'OPEN'

            statusFlag = request.session['statusFlag']
            logger.debug(statusFlag)
            statusResults = True
        else:
            logger.debug("List backlogs default flow : backlogStatus is not avaliable in request.GET")

        priorityResults = False
        priorityFlag = request.session.get('priorityFlag')
        if 'backlogPriority' in request.GET:
            logger.debug("Inside list_backlog_view backlogPriority")
            request.session['priorityFlag'] = None

            if "3" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '3'
            elif "4" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '4'
            elif "5" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '5'
            elif "6" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '6'
            elif "7" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '7'
            elif "8" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '8'
            elif "9" in request.GET.getlist("backlogPriority"):
                request.session['priorityFlag'] = '9'
            else:
                request.session['priorityFlag'] = '2'

            priorityFlag = request.session['priorityFlag']
            logger.debug(priorityFlag)
            priorityResults = True
        else:
             logger.debug("List backlogs default flow : backlogPriority is not avaliable in request.GET")
			 
        if statusResults and priorityResults:
            results = {'success': True}
            return JsonResponse(results)

        # Sprint Velocity and Average Team Velocity : START
        acceptedEstimateVel = self.evulateAcceptedVelocity(request, team_id)
        teamVelocity = self.evulateAvgTeamVelocity(request, team_id)
        logger.debug("Velocity in list_backlogs_view !!!!!! ")

        logger.debug(acceptedEstimateVel)
        request.session['acceptedVelocity'] = acceptedEstimateVel

        logger.debug(teamVelocity)
        request.session['teamVelocity'] = teamVelocity
        # Sprint Velocity and Average Team Velocity : END

        # From here now we have all we need to list the backlogs
        backlogs = retrieve_backlogs_by_project_status_and_priority(team_id, statusFlag, priorityFlag)\
            .order_by('project__name', 'priority', 'module', 'id')
		
        backlog_tuple = []
        from ...backlog.forms import AcceptanceCriteriaFormSet, EstimateForm, BacklogUpdateForm
        for backlog in backlogs:
            read_only = backlog.status.id == queued_status_id()

            estimate = get_object_or_none(Estimate, team_id=team_id, backlog_id=backlog.id)
            if not estimate:
                estimate = Estimate(team_id=team_id, backlog_id=backlog.id)

            # Creates the backlog form to edit data like story descr, skills,
            # notes, etc
            form = BacklogUpdateForm(read_only=read_only, instance=backlog, 
                                                prefix='backlog')

            # Creates the estimate form to edit the estimate time of the
            # specific backlog
            form_estimate = EstimateForm(instance=estimate, prefix='estimate')
            # Creates a set of forms that represents each acceptance
            # criteria linked to the specific backlog
            prefix = 'acceptance-criteria-%d' % backlog.id
            formset = AcceptanceCriteriaFormSet(instance=backlog,
                                                prefix=prefix)

            # Apeend all these information to be sent in the context
            backlog_tuple.append((backlog, form_estimate, form, formset),)

        page = request.GET.get('page', 1)
        paginator = Paginator(backlog_tuple,5)
        request.session['paginatorCount'] = paginator.count
        try:
            backlog_tuple_list = paginator.page(page)
        except PageNotAnInteger:
            backlog_tuple_list = paginator.page(1)
        except EmptyPage:
            backlog_tuple_list = paginator.page(paginator.num_pages)

        context = RequestContext(request, {'backlogs': backlog_tuple_list, })
        return render(request, 'backlog/backlog_list.html', context)

    def post(self, request):
        # Get volunteers team
        team_id = request.session.get('team')
        # Redirects to the index page if there is no team associated
        if team_id is None:
            return redirect('index')

        results = {'success': False}

        logger = logging.getLogger("alliance")
        logger.debug("Inside list_backlog_view request.POST")
        logger.debug(request.POST)
        if 'action-update-estimate' in request.POST:
            self.update_estimate(request, results, team_id)
        elif 'action-save' in request.POST:
            self.update_backlog_and_acc_cri(request, results)
        elif 'action-select-sprint':
            self.select_sprint(request, results)

        return JsonResponse(results)

    def update_estimate(self, request, results, team_id):
        from ...backlog.forms import EstimateForm

        backlog_id = request.POST.get('estimate-backlog_id')
        estimate = get_object_or_none(Estimate, team_id=team_id, backlog_id=backlog_id)
        form = EstimateForm(request.POST, prefix='estimate', instance=estimate)

        if form.is_valid():
            form.save()
            # TODO: What is happening in the next 3 lines??
            backlog = Backlog.objects.get(id=backlog_id)
            backlog.save()  # No need to save, we haven't made any changes
            backlog.refresh_from_db()  # No need to get an update from the db, we just got this object
            results['update_dttm'] = localtime(backlog.update_dttm)
            results['success'] = True
        else:
            results['errors'] = form.errors.as_json()

    def select_sprint(self, request, results):
        backlog_id = request.POST.get('backlog-id')
        sprint_id = request.POST.get('backlog-sprint')
        if not backlog_id:
            results['errors'] = create_json_message_object(
                "Please provide a valid Backlog.")
        elif not sprint_id:
            results['errors'] = create_json_message_object(
                "Please provide a valid Sprint.")
        else:
            try:
                team_id = request.session.get('team')
                # TODO: Should we validate if the user has privileges
                #  over this backlog and sprint before updating?
                backlog = Backlog.objects.get(id=backlog_id)
                # If the volunteer trying to update the sprint is not
                #  a member of the team that first selected the backlog
                #  then he/she is not allowed to execute the update.
                if not backlog.team or team_id == backlog.team.id:
                    sprint = Event.objects.get(id=sprint_id)
                    team = Team.objects.get(id=team_id)
                    backlog.sprint = sprint
                    backlog.team = team
                    if backlog.status.id == open_status_id():
                        status = Status.objects.get(id=selected_status_id())
                        backlog.status = status
                    backlog.save()
                    export_to_github(backlog)
                    backlog.refresh_from_db()

                    results['status'] = backlog.status.name
                    if backlog.update_dttm:
                        results['update_dttm'] = localtime(backlog.update_dttm)
                    results['sprintName'] = str(sprint)
                    results['success'] = True
                else:
                    results['errors'] = create_json_message_object(
                        "This backlog was previously selected by another" +
                        " team and can only be updated by a member of" +
                        " that team.")
            except Event.DoesNotExist:
                results['errors'] = create_json_message_object(
                    "Sprint does not exist.")
            except Backlog.DoesNotExist:
                results['errors'] = create_json_message_object(
                    "Backlog does not exist.")
            except Status.DoesNotExist:
                results['errors'] = create_json_message_object(
                    "Status does not exist.")
            except Exception as e:
                results['errors'] = create_json_message_object(
                    str(e), code="exception")

    def update_backlog_and_acc_cri(self, request, results):
        from ...backlog.forms import AcceptanceCriteriaFormSet, BacklogUpdateForm

        backlog_id = request.POST.get('backlog-id')
        backlog = get_object_or_none(Backlog, id=backlog_id)
        form = BacklogUpdateForm(request.POST,
                                 prefix='backlog',
                                 instance=backlog)

        prefix = 'acceptance-criteria-%d' % backlog.id
        formset = AcceptanceCriteriaFormSet(request.POST,
                                            instance=backlog,
                                            prefix=prefix)
        if form.is_valid():
            if formset.is_valid():
                backlog = form.save()
                backlog.refresh_from_db()
                formset.save()
                formset = AcceptanceCriteriaFormSet(instance=backlog, prefix=prefix)
                html = render_to_string('backlog/acc_cri_par.txt',
                                        {'form': form, 'formset': formset})
                results['html'] = html
                results['mgt_fields'] = formset.management_form.as_p()
                results['update_dttm'] = localtime(backlog.update_dttm)
                results['success'] = True
            else:
                results['errors'] = formset.non_form_errors()
        else:
            results['errors'] = form.errors.as_json()

    def evulateAcceptedVelocity(self, request, teamId):
        logger = logging.getLogger("alliance")
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

            if not acceptedEstimate:
                acceptedEstimate = 0
                logger.debug("Accepted Estimate is EMPTY. Resetting to ZERO(0) ", acceptedEstimate)

            if acceptedSprint != None and acceptedEstimate != None:
                acceptedEstimateVel += int(acceptedEstimate)

        return acceptedEstimateVel


    def evulateAvgTeamVelocity(self, request, teamId):
        logger = logging.getLogger("alliance")

        # Average Team Velocity for Completed backlogs : START
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

            if estimateValue == "" or estimateValue is None:
                estimateValue = 0

            if bgCountBySprint == 0:
                previousRecSprint = currentRecSprint

            if currentRecSprint == previousRecSprint:
                bgCountBySprint += 1
                estimateList.append(int(estimateValue))
            else:
                bgCountBySprint = 1

                if previousRecSprint != None:
                    myTeamVelocitydict.update({previousRecSprint: estimateList})

                estimateList = []
                estimateList.append(int(estimateValue))

            previousRecSprint = currentRecSprint

        if previousRecSprint != None:
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
        return teamVelocity