from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('details/<int:student_id>/', views.details, name='details'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_course_to_student/<int:student_id>/', views.add_course_to_student, name='add_course_to_student'),
]
