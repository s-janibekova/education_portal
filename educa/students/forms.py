from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser


class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = SimpleUser
        fields = ('email', 'username', 'userImg', 'group')


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('email', 'username', 'userImg', 'group')


















# from django import forms
# from courses.models import Course
#
#
# class CourseEnrollForm(forms.Form):
#     course = forms.ModelChoiceField(queryset=Course.objects.all(),
#                                     widget=forms.HiddenInput)
