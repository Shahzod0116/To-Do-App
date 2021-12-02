from django.urls import path
from .views import (HomePageView,
HomeDetailView,
HomeCreateView,
HomeUpdateView,
HomeDeleteView)

urlpatterns = [
    path('todo/<int:pk>/delete/',HomeDeleteView.as_view(),name='todo_delete'),
    path('todo/<int:pk>/edit',HomeUpdateView.as_view(),name='todo_edit'),
    path('todo/new/',HomeCreateView.as_view(),name='todo_new'),
    path('todo/<int:pk>/',HomeDetailView.as_view(),name='detail'),
    path('',HomePageView.as_view(),name='home'),
]