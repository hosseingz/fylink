from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ['chat_id', 'traffic', 'wallet']


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class DownloadListSerializers(serializers.ModelSerializer):
    class Meta:
        model = DownloadList
        fields = '__all__'

    def update_file(self, data):
        self.fields['file'] = data


class SubscriptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
