from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        title = forms.CharField(label='title', max_length=100)
        fields = '__all__'
