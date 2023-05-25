from django.urls import path

from . import views

app_name = "cvgen"
urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('skill_form', views.create_skill_form, name="skill_form"),
    path('<int:pk>/resume', views.create_skill, name="resume"),
    path('qualification_form', views.create_qualification_form,name="qualification_form"),
    path('emp_form', views.create_employment_history_form, name="emp_form"),
    path('edu_form', views.create_education_history_form,name="edu_form"),
    path('<int:pk>/resumedetails',views.resumedetails,name="resumedetails"),
    path('<int:pk>/user_info', views.user_info, name="user_info")
]
