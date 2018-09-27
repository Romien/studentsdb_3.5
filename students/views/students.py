# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Student


def students_list(request):
    students = Student.objects.all()

    #students = students.order_by("last_name")
    #students = students.order_by("last_name").reverse()
    #students = students.order_by("ticket")
    #students = students.order_by("ticket").reverse()


# try to order student list
    order = request.GET.get('order_by', '')
    if order in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()


# paginate students
    paginator = Paginator(students, 3)  # Show 3 students per page
    # ми отримуємо номер поточної сторінки, для якої ми маємо зібрати(?) студентів. По замовчуванню це буде перша.
    page = request.GET.get('page')
    try:
        # students тут тепер це не простий список QuerySet, а це тепер спеціальний wrapper, педжінейтор пейдж, який має цілий набір методів.
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    # groups = (
    #     {'id': 1,
    #      'name': u'МВ-51',
    #      'leader': {'id': 1, 'name': u'Джон Сендвік'}},
    #     {'id': 2,
    #      'name': u'МВ-52',
    #      'leader': {'id': 2, 'name': u'Майкл Ліндсі'}},
    # )

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('Here we will have a form')


def students_edit(request, sid):
    return HttpResponse('students %s Edit Form' % sid)


def students_attend(request, sid):
    return HttpResponse('student %s Attend Form' % sid)


def students_delete(request, sid):
    return HttpResponse('student %s Delete Form' % sid)
