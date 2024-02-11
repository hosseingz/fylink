from django import forms
from .models import BotUser, File


class NewUserForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = ['chat_id', 'username']

    def clean_chat_id(self):
        chat_id = self.cleaned_data['chat_id']

        if BotUser.objects.filter(chat_id=chat_id).exists():
            raise forms.ValidationError("This user already exist")

        return chat_id


class FileForm(forms.ModelForm):
    chat_id = forms.CharField(max_length=250)

    class Meta:
        model = File
        fields = ['file_id', 'file_name', 'file_extension', 'file_path', 'file_size']


class CheckAttrForm(forms.forms):
    chat_id = forms.CharField(max_length=250)
    attr = forms.CharField(max_length=250)




