from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/<int:id>/', views.subject, name='subject'),
    path('subjects/edit/<int:id>/', views.edit_subject, name='edit_subject'),
    path('subjects/new/', views.new_subject, name='new_subject')
]
