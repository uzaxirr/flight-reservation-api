from django.urls import path
from .views import ListStu, DetailedStu
urlpatterns = [
    path('students/', ListStu.as_view()),
    path('student/<int:pk>', DetailedStu.as_view())
]
