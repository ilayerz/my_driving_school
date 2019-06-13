from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    students = User.objects.filter(groups__name='Student')
    return render(request, 'instructor/index.html', {'studentslist': students})

def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    if student:
        return render(request, 'instructor/student.html', {'student': student})
