from django.forms import ModelForm

from .models import *

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= '__all__'