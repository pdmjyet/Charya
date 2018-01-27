import datetime
import json
from GoalApp import models

def getCurrentDayGoals(date, user):
    day = date.weekday()
    month = date.month()
    goalsList = models.Goal.objects.filter(UserID = user.pk, dateCreated.month() = month)
    goalsListApplicable = []
    for goal in goalsList:
        metric = getCurrentDayGoalMetric(date, goal.metrics)
        if metric != 'N/A':
            goalsListApplicable.append(goal)
    return goalsListApplicable

def getCurrentDayGoalMetric(date, metricsJson):
    metrics = json.load(metricsJson)
    if str(date.weekday()) not in metrics:
        raise Exception("Metrics not found for given day : ". date)
    return metrics[str(day)]

def updateGoalWeightage(goalsListApplicable):
    total = 0
    for goal in goalsListApplicable:
        total += goal.weightage
    for goal in goalsListApplicable:
        goal.weightage = float((goal.weightage * 100)/total)
    return goalsListApplicable

def getGoalScoreGivenMinLimit(min_expected, actual):
    #[min:max]
    #test commit by Sri
    # TODO : handle [:y] case when max limit is not known for penality calculation
    if(actual >= min_expected):
        return 5050
    normalize_to_zero_hundred = int((actual*100)/min_expected)
    a = float(((normalize_to_zero_hundred)*(normalize_to_zero_hundred+1))/2)
    return score
