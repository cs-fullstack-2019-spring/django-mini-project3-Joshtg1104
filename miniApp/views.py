from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TeachTimeForm, TeacherTimeModel


# Create your views here.

def index(request):
    registries = TeacherTimeModel.objects.all()
    context = {
        "registries": registries
    }
    return render(request, 'miniApp/index.html', context)


def timecard(request):
    timeregistry = TeachTimeForm(request.POST or None)
    if timeregistry.is_valid():
        timeregistry.save()
        return redirect('index')
    context = {
        "timeregistry": timeregistry
    }
    return render(request, 'miniApp/registry.html', context)

def edit(request, id):
    cardedit = get_object_or_404(TeacherTimeModel, pk=id)
    timeedit = TeachTimeForm(request.POST or None, instance=cardedit)
    if timeedit.is_valid():
        timeedit.save()
        return redirect('index')
    context = {
        "timeregistry": timeedit
    }
    return render(request, 'miniApp/registry.html', context)
