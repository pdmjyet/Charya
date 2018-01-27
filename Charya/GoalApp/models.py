from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='user_profile_pics', blank=True)

    def __str__(self):
        return self.user.username;


class Goal(models.Model):
    UserID = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=200, null= False)
    description = models.TextField(null=True)
    weightage = models.FloatField(default=0.0)
    ###########################################
    # json representation of all days of a week
    # {
    #    "0": [min:max]
    #       "2": "N/A"
    #}
    # 0 -> Monday
    # min/max empty => no boundary
    metrics = models.TextField()
    metricsUnit = models.CharField(max_length=10)
    dateCreated = models.DateTimeField(default=timezone.now())

    # weekday number 0-6 , mon to sun
    def isApplicable(self, day):
        data = json.parse(self.metrics)
        if data[day] == "N/A":
            return False
        return True

    def getWeekdayMetric(self, day):

        self.metrics

class Status(models.Model):
    goalID = models.ForeignKey(Goal)
    date = models.DateTimeField(default = timezone.now())
    metric = models.FloatField(default=0.0)

class Score(models.Model):
    date = models.DateTimeField(null=True)
    score = models.FloatField(default=0.0)
    userID = models.ForeignKey(UserProfile)

    def updateScoreAndDate(self, scoredate, score):
        self.score = score
        self.Date = scoredate

    # TODO
    def calculateDailyScore(self, date):
        pass

    # TODO  ##
    def computeCurrentWeekScore(self):
        date = timezone.now()

class Group(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    partner1 = models.ForeignKey(UserProfile, related_name="partner1")
    partner2 = models.ForeignKey(UserProfile, related_name="partner2")

    def __str__(self):
        return self.name
