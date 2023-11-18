from django import forms
from .models import Task, TaskGroup


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TaskGroupCreateForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
        }


class TaskGroupUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['name', 'is_done']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
