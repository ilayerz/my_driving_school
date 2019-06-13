from django.shortcuts import render
from django.contrib.auth.models import User
from drivingapp.models import Planning


def home(request):
    students = User.objects.filter(groups__name='Student')
    plannings = Planning.objects.filter(id_instructor=request.user.id)
    return render(request, 'instructor/index.html', {'studentslist': students, 'planninglist': plannings})

def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    if student:
        return render(request, 'instructor/student.html', {'student': student})
