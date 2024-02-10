from django import forms
from .models import BotUser


class NewUserForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = ['chat_id', 'username']

    def clean_chat_id(self):
        chat_id = self.cleaned_data['chat_id']

        if BotUser.objects.filter(chat_id=chat_id).exists():
            raise forms.ValidationError("This user already exist")

        return chat_id


