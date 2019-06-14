from django.shortcuts import render
from django.contrib.auth.models import User
from drivingapp.models import Planning
from django.shortcuts import redirect

def home(request):
    students = User.objects.filter(groups__name='Student')
    plannings = Planning.objects.filter(id_instructor=request.user.id)
    return render(request, 'instructor/index.html', {'studentslist': students, 'planninglist': plannings})

def delete(request, id):
    planning = Planning.objects.get(id=id)
    if planning:
        planning.delete()
        return redirect('instructor')

def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    if student:
        return render(request, 'instructor/student.html', {'student': student})
