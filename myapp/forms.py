from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# from .models import File


class SignUpForm1(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    bio = forms.CharField(max_length=500, required=False, help_text='Optional.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(required=False, help_text='Optional. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'location', 'birth_date')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        profile = Profile.objects.create(user=user, bio=self.cleaned_data['bio'], location=self.cleaned_data['location'], birth_date=self.cleaned_data['birth_date'])
        return user




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



# class FileForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ('name', 'file',)
