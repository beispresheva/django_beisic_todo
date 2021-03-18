from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task, Label, Priority
from django.urls import reverse


# Custom Functions for Views
# def get_all_tasks():
#     all_tasks = Task.objects.all().filter(author=User)

def custom_get_user(request):
    current_user = request.user
    return current_user

def landing(request):
    return render(request, 'todo/landing.html', {'title': 'Welcome'})

@login_required
def index(request):
    current_user = request.user
    context = {
        'tasks': Task.objects.all().filter(author=current_user)
    }
    return render(request, 'todo/index.html', context)

@login_required
def today(request):
    return render(request, 'todo/today.html', {'title': 'Today Tasks'})

@login_required
def upcoming(request):
    return render(request, 'todo/upcoming.html', {'title': 'Upcoming Tasks'})

@login_required
def priority(request):
    current_user = request.user
    context = {
        'tasks': Task.objects.all().filter(author=current_user)
    }
    return render(request, 'todo/priority.html', context)

@login_required
def label(request):
    context = {
        'title': 'Labels',
        'labels': Label.objects.all()
    }
    return render(request, 'todo/label.html', context)


# Label Functions
class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['label']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo-label')


def display_label(request):
    result=respond.Get['custom-labels']
    return render(request, 'todo/label.html', {'customLabels': result})


class LabelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Label

    def test_func(self):
        label = self.get_object()
        if self.request.user == self.request.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse('todo-label')


# Task Functions
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'taskdate', 'priority', 'label']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo-index')

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'taskdate', 'priority', 'label']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

    def get_success_url(self):
        return reverse('todo-index')

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

    def get_success_url(self):
        return reverse('todo-index')