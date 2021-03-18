from django.urls import path
from .views import LabelCreateView, LabelDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView
from . import views


urlpatterns = [
    path('', views.landing, name="todo-landing"),
    path('todo/', views.index, name="todo-index"), 
    path('todo/today/', views.today, name="todo-today"),
    path('todo/upcoming/', views.upcoming, name="todo-upcoming"),
    path('todo/priority/', views.priority, name="todo-priority"),
    path('todo/label/', views.label, name="todo-label"),
    path('todo/label/new/', LabelCreateView.as_view(), name='label-create'),
    path('todo/label/<int:pk>/delete/', LabelDeleteView.as_view(), name="label-delete"),
    path('todo/task/new/', TaskCreateView.as_view(), name='task-create'),
    path('todo/task/<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
    path('todo/task/<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete")
]