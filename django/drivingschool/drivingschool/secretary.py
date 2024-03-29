from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from drivingapp.models import Planning


def home(request):
    instructors = User.objects.filter(groups__name='Instructor')
    students = User.objects.filter(groups__name='Student')
    return render(request, 'secretary/index.html', {'instructorslist': instructors, 'studentslist': students})

def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    studentPlannings = Planning.objects.filter(id_student=id)
    instructor = User.objects.filter(groups__name='Instructor')
    if student:

        return render(request, 'secretary/student.html', {'student': student, 'plannings': studentPlannings, 'instructors': instructor})

def addUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST['role'])
            user.groups.add(group)
            return redirect('secretary')

    form = UserCreationForm()
    return render(request, 'secretary/form.html', {'form': form})

def deleteUser(request):
    User.objects.filter(username=request.POST['username']).delete()
    return redirect('secretary')

def delete(request, id):
    user = User.objects.get(id=id)
    if user:
        user.delete()
        return redirect('secretary')
