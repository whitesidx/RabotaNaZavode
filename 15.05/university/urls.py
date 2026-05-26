from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    path('teachers/', views.teachers, name="teachers"),
    path('contacts/', views.contacts, name="contacts"),
]
