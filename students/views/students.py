# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Джанґо',
         'last_name': u'Фрімен',
         'ticket': 235,
         'image': 'static/img/django.jpeg'},
        {'id': 2,
         'first_name': u'Біллі',
         'last_name': u'Креш',
         'ticket': 2123,
         'image': 'static/img/billy.jpeg'}
    )
    groups = (
        {'id': 1,
         'name': u'МВ-51',
         'leader': {'id': 1, 'name': u'Джон Сендвік'}},
        {'id': 2,
         'name': u'МВ-52',
         'leader': {'id': 2, 'name': u'Майкл Ліндсі'}},
    )

    return render(request, 'students/students_list.html', {'students': students, 'groups': groups})


def students_add(request):
    return HttpResponse('Here we will have a form')


def students_edit(request, sid):
    return HttpResponse('students %s Edit Form' % sid)


def students_attend(request, sid):
    return HttpResponse('student %s Attend Form' % sid)


def students_delete(request, sid):
    return HttpResponse('student %s Delete Form' % sid)
