from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'todo/index.html')

def today(request):
    return render(request, 'todo/today.html', {'title': 'Today Tasks'})

def upcoming(request):
    return render(request, 'todo/upcoming.html', {'title': 'Upcoming Tasks'})

def priority(request):
    return render(request, 'todo/priority.html', {'title': 'Priorities'})

def label(request):
    return render(request, 'todo/label.html', {'title': 'Labels'})