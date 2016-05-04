from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import List


class PostForm(ModelForm):
    class Meta:
        model = List
        fields = ('title', 'text')