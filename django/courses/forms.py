from django import forms
from .models import Course, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'short_description', 'description')


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('subject', 'description', 'order')