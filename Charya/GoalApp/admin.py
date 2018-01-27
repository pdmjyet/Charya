from django.contrib import admin
from GoalApp import models
# Register your models here.



class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'partner1', 'partner2', 'pk')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile_pic')

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Goal)
