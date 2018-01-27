from django.shortcuts import render
from GoalApp import forms, models
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView)
# Create your views here.


class CreateGroupView(CreateView):
    form_class = forms.GroupForm
    model = models.Group

    def form_valid(self, form):
        user1 = get_object_or_404(UserProfile, username = form['partner1_username'])
        user2 = get_object_or_404(UserProfile, username = form['partner2_username'])
        del form['partner1_username']
        del form['partner2_username']
        form['partner1_ID'] = user1.pk
        form['partner2_ID'] = user2.pk
        return super(CreateGroupView, self).form_valid(form)

#########################################################################################
@login_required
def group_details(request, pk):
    group = get_object_or_404(models.Group, pk=pk)
    user1 = models.UserProfile.objects.get(username = group.partner1_ID)
    user2 = models.UserProfile.objects.get(username = group.partner2_ID)
    return render(request, 'GoalApp/group_detail.html', {'group': group, 'user1': user1, 'user2': user2})

@login_required
def userprofile_details(request, pk):
    userprofile = get_object_or_404(models.UserProfile, pk=pk)
    groups = models.Group.objects.filter(Q(partner1_ID = userprofile.pk) | Q(partner2_ID=userprofile.pk))
    return render(request, 'GoalApp/userprofile_detail.html', {'groups': groups, 'user': userprofile})
