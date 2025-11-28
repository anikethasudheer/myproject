from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'student/home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        Student.objects.create(name=name, age=age)
        return redirect('/')
    return render(request, 'student/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.save()
        return redirect('/')
    return render(request, 'student/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')
