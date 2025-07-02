from django.urls import path

from blog.views import home, add_student, update_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('add-student/', add_student, name='add_student'),
    path('update-student/<int:student_id>/', update_student, name='update_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student')
]
