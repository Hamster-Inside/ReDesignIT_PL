from django import forms
from .models import Task, TaskGroup


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value of is_done to False (unchecked)
        self.initial['is_done'] = False


class TaskGroupForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['name', 'is_done']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Set the initial value of is_done to False (unchecked)
            self.initial['is_done'] = False
