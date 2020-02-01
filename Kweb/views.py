from django.shortcuts import render
from .models import Project
# Create your views here.


def home(request):
    projects = Project.objects
    return render(request, 'kweb/homes.html', {'projects': projects})