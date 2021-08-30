from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectsPage, name='projects')
]
