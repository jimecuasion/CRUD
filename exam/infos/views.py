from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .filters import StudentFilter


# Create your views here.
def home(request):
    students = Student.objects.all()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'myFilter': myFilter
    }
    return render(request, 'infos/dashboard.html', context)

def student(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,
    }
    return render(request, 'infos/student.html', context)

def addStudent(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'infos/student_form.html', context)

def updateStudent(request, pk):

    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }
    return render(request, 'infos/student_form.html', context)

def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == "POST":
        student.delete()
        return redirect('/')

    context = {
        'student': student,
    }
    return render(request, 'infos/delete.html', context)