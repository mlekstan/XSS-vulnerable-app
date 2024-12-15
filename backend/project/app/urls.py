from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/reflected_xss/", views.reflected_xss, name="reflected_xss"),
    path("tasks/stored_xss", views.stored_xss, name="stored_xss"),
    path("tasks/dom_xss/", views.dom_xss, name="dom_xss"),
    path("tasks/stored_xss/add_comment", views.add_comment, name="add_comment"),
    path("tasks/stored_xss/delete_comment/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]