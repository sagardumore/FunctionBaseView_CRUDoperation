from django import  forms
from .models import Laptop
from django.core import validators

class LaptopModelForm(forms.ModelForm):
    class Meta :
        model = Laptop
        fields = '__all__'
        labels = {
            'ram': 'RAM in GB',
            'company': 'COMPANY NAME'
        }
        widgets = {
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'for ex. abc123'
                }
            ),'ram': forms.TextInput(
                attrs={
                    'placeholder': 'for ex.2GB,4GB,8GB'
                }
            ),'rom': forms.TextInput(
                attrs={
                    'placeholder': 'for ex. 1TB,2TB'
                }
            )
        }

        def clean_company(self):
            c = self.cleaned_data['company']
            capital = c.capitalize()
            if c != capital:
                raise forms.ValidationError('Please enter first charactor is capital')
            return c

        def clean_ram(self):
            r = self.cleaned_data['ram']
            if r < 1:
                raise forms.ValidationError('Ram can not be less than 1GB')
            else:
                return r
        def clean_rom(self):
            ro = self.cleaned_data['rom']
            if ro < 1:
                raise forms.ValidationError('Ram can not be less than 1GB')
            else:
                return ro

        def clean_weight(self):
            w = self.cleaned_data['weight']
            if w < 0:
                raise forms.ValidationError('weight can not be negative')
            else:
                return w




