from django.shortcuts import render, get_object_or_404
from courses.models import Course
from .models import Student


# Create your views here.

def students_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.filter(courses=course).order_by('name')
    return render(request, 'students/students_list.html', {'students': students})


def students_full_list(request):
    students = Student.objects.order_by('name')
    return render(request, 'students/students_list.html', {'students': students})


def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
