from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'date_of_birth',
                  'email', 'phone', 'address', 'skype',
                  'courses')
