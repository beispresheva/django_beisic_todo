from django.urls import path
from .views import LabelCreateView, LabelDeleteView
from . import views


urlpatterns = [
    path('', views.index, name="todo-index"),
    path('today/', views.today, name="todo-today"),
    path('upcoming/', views.upcoming, name="todo-upcoming"),
    path('priority/', views.priority, name="todo-priority"),
    path('label/', views.label, name="todo-label"),
    path('label/new/', LabelCreateView.as_view(), name='label-create'),
    path('label/<int:pk>/delete/', LabelDeleteView.as_view(), name="label-delete")
]