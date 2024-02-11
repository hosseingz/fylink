from django.shortcuts import render, HttpResponse
from django.db.models import Count

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .serializers import *

from .forms import *
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


# Create your views here.
def index(request):
    return HttpResponse("salam amu")


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


@api_view(['GET'])
def get_files(request):
    query = File.objects.all()
    serializer = FileSerializers(query, many=True)
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def user_info(request):
    user = BotUser.objects.get(chat_id=request.GET.get('chat_id'))
    serializer = UserSerializers(user)
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def download_list(request):
    List = DownloadList.objects.all()
    serializer = DownloadListSerializers(List, many=True)
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def check_Subscription(request):
    
    form = CheckAttrForm(request.Post)
            
    if form.is_valid:
        cd = form.cleaned_data
        user = BotUser.objects.get(chat_id=cd['chat_id'])
        if hasattr(user, cd['attr']):
            sub_obj = Subscription.objects.get(chat_id=cd['chat_id'])
            serializer = SubscriptionsSerializers(sub_obj)
            return Response(data=serializer.data, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_download_list(request):
    form = FileForm(request.POST)
    if form.is_valid():
        file = form.save()
        cd = form.cleaned_data
        DownloadList(chat_id=cd['chat_id'], file=file).save()

        return Response(status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)