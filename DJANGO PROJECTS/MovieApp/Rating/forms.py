from django.forms import ModelForm, widgets
from Rating.models import User
from django import forms

# create a ModelForm


class registerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['first_name', 'Last_name', 'gender',
                  'date_of_birth', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'name': 'firstname',
                    'class': 'form-control',
                    'placeholder': 'First name',
                    'type': 'text',
                }
            ),
            'Last_name': forms.TextInput(
                attrs={
                    'name': 'lastname',
                    'class': 'form-control',
                    'placeholder': 'Last name',
                    'type': 'text'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'name': 'gender',
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    'name': 'date',
                    'class': 'form-control',
                    'placeholder': 'DOB',
                    'type': 'date',
                    'value': '19-08-2011',
                    'id': 'example-date-input'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'name': 'email',
                    'class': 'form-control',
                    'placeholder': 'Email Address',
                    'type': 'email'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'name': 'phone',
                    'class': 'form-control',
                    'placeholder': 'Phone Number',
                    'type': 'text'
                }
            ),
        }
