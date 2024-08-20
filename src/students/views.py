from django.shortcuts import render, redirect
from .form import SummaryStudentForm
from .models import SummaryStudent

def student_create_view(request):
    form = SummaryStudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SummaryStudentForm()

    context = {
        'form': form
    }
    return render(request, 'students/student_create_view.html', context)

def student_list_view(request):
    students = SummaryStudent.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list_view.html', context)


# def student_name_view(request):
#     students = SummaryStudent.objects.all()
#     context = {
#         'students': students
#     }
#     return render(request, 'students/student_name_view.html', context)