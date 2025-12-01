from django import forms
from .models import Section

class BlockForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'vacation_type','min_visits','max_visits']
        widgets = {

        }