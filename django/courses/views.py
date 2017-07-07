from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


# Create your views here.


def courses_list(request):
    courses = Course.objects.order_by('name')
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course=pk).order_by('order')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})
