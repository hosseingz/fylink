from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import login_required
from django.views.decorators.http import require_POST
from .forms import NewUserForm
from .models import *

import json


def check_date(date, delta, model):
    tomorrow = date + datetime.timedelta(days=delta)
    today = datetime.date.today()
    if today < tomorrow:
        return model.objects.get(date=date)
    else:
        new_obj = model()
        return new_obj



# Todo Hameye Commends ha Post Beshe


def checkAPI(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        # act 1
        func(*args, **kwargs)
        # act 2

    return wrapper


# Create your views here.
def index(request):
    return None


# Commends
def new_user(request):
    # Todo add 1 to daily report
    form = NewUserForm(request.GET)
    data = {'status': 204}  # None Content
    if form.is_valid():
        form.save()
        data = {
            'status': 200  # New User Saved !
        }
        today = check_date(DailyReport.objects.last().date, 1, DailyReport)
        today.new_users += 1
        today.save()

    data = json.dumps(data)

    return HttpResponse(data)


