from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["num", "opisanie", "status"]
        widgets = {
            "num": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер'
        }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
            ,  "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберете из списка'
            })
        }