from django.shortcuts import render
def home(request):
    return render(request, 'secretary/index.html')
