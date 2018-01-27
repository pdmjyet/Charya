from django import forms
from GoalApp import models
from django.contrib.auth.models import User
from GoalApp import constants

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = models.UserProfile
        fields = ('profile_pic',)

class GroupForm(forms.ModelForm):
    partner1_username = forms.CharField(widget=forms.TextInput())
    partner2_username = forms.CharField(widget=forms.TextInput())
    class Meta():
        model = models.Group
        fields = ('name', 'description')

class GoalForm(forms.ModelForm):
    class Meta():
        model = models.Goal
        fields = ('title', 'description', 'weightage', 'metricsUnit')
