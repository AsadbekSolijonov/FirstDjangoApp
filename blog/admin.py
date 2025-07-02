from django.contrib import admin

from blog.models.students import Student
from blog.models.blog import Blog

admin.site.register(Student)
admin.site.register(Blog)
