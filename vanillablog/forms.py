from django.forms import ModelForm
from .models import List


class PostForm(ModelForm):
    class Meta:
        model = List
        fields = ('title', 'text')