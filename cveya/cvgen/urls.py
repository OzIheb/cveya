from django.urls import path

from . import views

app_name = "cvgen"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:skill_id>/details/", views.details,name="details"),
    path('register/', views.register, name='register'),
    path('resume/', views.createResume, name="createresume")
]
