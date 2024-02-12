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


@api_view(['POST'])
def new_user(request):
    # Todo add 1 to daily report
    form = NewUserForm(request.POST)
    status = HTTP_400_BAD_REQUEST  # None Content
    
    if form.is_valid():
        form.save()
        status =  HTTP_200_OK
        today = check_date(DailyReport.objects.last().date, 1, DailyReport)
        today.new_users += 1
        today.save()


    return Response(status=status)


@api_view(['POST'])
def files(request):
    query = File.objects.filter(is_active=True)
    serializer = FileSerializers(query, many=True)
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def download_list(request):

    # Todo bijur update elaki filin tamam etelagatin geyrarsin
    objects = DownloadList.objects.all()
    serializer = DownloadListSerializers(objects, many=True)

    for i, item in enumerate(serializer.data):
        item.update({'file': FileSerializers(objects[i].file).data})

    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def check_Subscription(request):

    form = CheckAttrForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        user = BotUser.objects.get(chat_id=cd['chat_id'])
        print(user.__dict__)

        if hasattr(user, cd['attr']):
            sub_obj = Subscription.objects.get(user=user)
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


@api_view(['POST'])
def whose_turn_is_it(request):
    obj = DownloadList.objects.first()
    serializer = DownloadListSerializers(obj)
    serializer.update_file(FileSerializers(obj.file))
    return Response(data=serializer.data, status=HTTP_200_OK)