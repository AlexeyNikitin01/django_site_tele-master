from django.forms import ModelForm, TextInput
from .models import RepairOrder


class RepairOrderForm(ModelForm):
    class Meta:
        model = RepairOrder
        fields = ['name', 'surname', 'phone', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон +7 --- --- -- --',
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание дефекта',
            })
        }
