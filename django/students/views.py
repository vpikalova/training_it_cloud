from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, HttpResponseRedirect
from courses.models import Course
from .models import Student
from .forms import StudentForm

from django.contrib.auth.decorators import login_required


# Create your views here.

def students_list(request):
    pk = request.GET.get('course_id', '-1')
    if '-' in pk or pk == '':
        students = Student.objects.all().order_by('name')
    else:
        course = get_object_or_404(Course, pk=pk)
        students = Student.objects.filter(courses=course).order_by('name')
    return render(request, 'students/students_list.html', {'students': students})


def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_new(request):
    if (request.method == "POST"):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            student = form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        course_id = request.GET.get('course_id', '-1')
        if '-' in course_id or course_id=='':
            form = StudentForm()
        else:
            course = get_object_or_404(Course, pk=course_id)
            form = StudentForm(initial={'courses': [course]})
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if (request.method == "POST"):
        form = StudentForm(request.POST, instance=student)
        if (form.is_valid()):
            student = form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form})

@login_required
def student_remove(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    next = request.GET.get('next', '/')
    return HttpResponseRedirect(next)