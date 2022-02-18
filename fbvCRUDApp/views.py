from django.shortcuts import render, redirect
from fbvCRUDApp.models import Student
from fbvCRUDApp.forms import StudentForm


# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    return render(request, "fbvCRUDApp/index.html", {"students": students})


def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, "fbvCRUDApp/create.html", {"form": form})


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")


def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "fbvCRUDApp/update.html", {"form": form})
