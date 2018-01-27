from django.conf.urls import url
from GoalApp import views

app_name = "GoalApp"
urlpatterns = [
    url(r'^user/(?P<pk>\d+)/$', views.userprofile_details, name='userprofile_detail' ),
    url(r'^group/$', views.CreateGroupView.as_view(), name='group_create' ),
]
