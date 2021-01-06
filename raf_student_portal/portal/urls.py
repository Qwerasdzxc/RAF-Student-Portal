from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/<int:id>/', views.subject, name='subject'),
    path('subjects/edit/<int:id>/', views.edit_subject, name='edit_subject'),
    path('subjects/new/', views.new_subject, name='new_subject'),
    path('subjects/news/new/', views.new_news, name='new_news'),
    path('subjects/<int:subject_id>/delete-news/<int:news_id>/', views.delete_news, name='delete_news'),
]
