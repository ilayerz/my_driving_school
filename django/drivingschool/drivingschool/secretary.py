from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    instructors = User.objects.filter(groups__name='Instructors')
    students = User.objects.filter(groups__name='Student')
    return render(request, 'secretary/index.html', {'instructorslist': instructors, 'studentslist': students})

def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    if student:

        return render(request, 'secretary/student.html', {'student': student})
