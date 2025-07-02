from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms.students import UserCreationForm
from blog.models.students import Student


@login_required
def home(request):
    student = Student.objects.all()
    search_student = request.GET.get('search_q')  # AL
    if search_student:
        student = Student.objects.filter(
            Q(first_name__icontains=search_student) | Q(last_name__icontains=search_student) | Q(
                phone__icontains=search_student))

    context = {
        "students": student
    }
    return render(request, 'blog/students.html', context=context)


@login_required
def add_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/add_student.html', {'form': form})


@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm(instance=student)
    context = {'form': form, 'student': student}
    return render(request, 'blog/update_student.html', context=context)


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'blog/delete_student.html', {'student': student})
