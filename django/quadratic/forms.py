from django import forms
from .models import Quadratic

class QuadraticForm(forms.ModelForm):
    class Meta:
        model = Quadratic
        fields = ('a', 'b', 'c')