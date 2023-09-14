from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# from .models import File

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class FileUploadForm(forms.Form):
    file = forms.FileField()


class ParagraphForm(forms.Form):
    paragraph = forms.CharField(widget=forms.Textarea)

# class AIbotForm(forms.Form):
#     query = forms.CharField(widget=forms.Textarea)


# class FileForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ('name', 'file',)
