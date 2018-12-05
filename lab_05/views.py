from django.http import HttpResponse
from django.shortcuts import render
from lab_05 import dbFacade


def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html')


def universityInfo(request):
    return render(request, 'universityInf.html', dbFacade.getUniversityInfo())
