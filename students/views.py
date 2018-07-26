from django.shortcuts import render

# Create your views here.


def student_list(request):
    return render(request, 'students/students_list.html', {})
