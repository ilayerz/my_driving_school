"""drivingschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from drivingschool import login, secretary, instructor, student

urlpatterns = [
    path('driving/', include('drivingapp.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('secretary/', secretary.home, name="secretary"),
    path('secretary/student/<int:id>', secretary.student, name="studentfromsecretary"),
    path('test/', login.home),
    path('instructor/', instructor.home, name="instructor"),
    path('instructor/student/<int:id>', instructor.student, name="studentfrominstructor"),
    path('adduser/', secretary.addUser, name="adduser"),
    path('deleteuser/', secretary.deleteUser, name="deleteuser"),
    path('instructor/form/<int:id>', student.renderForm, name="studentform"),
    path('student/planning/', student.getPlanning, name="studentplanning")
]
