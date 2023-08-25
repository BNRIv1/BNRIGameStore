from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from EShopApp.models import VideoGame, EShopUser


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class VideoGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VideoGameForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    #
    class Meta:
        model = VideoGame
        exclude = ("user",)
