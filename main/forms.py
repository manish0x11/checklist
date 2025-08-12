from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'user', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter task', 'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'})
        }

class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
        widgets = {
            'status': forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}),
        }


