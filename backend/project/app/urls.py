from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/reflected_xss/", views.reflected_xss, name="reflected_xss"),
    path("tasks/stored_xss", views.stored_xss, name="stored_xss"),
    path("tasks/dom_xss/", views.dom_xss, name="dom_xss")
]