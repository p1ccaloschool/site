from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
]