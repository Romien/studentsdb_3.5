# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def exams_list(request):
    exams = (
        {'id': 1,
         'title': u'Теорія інформатики',
         'date': '20-03-2018',
         'teacher': u'Франсуа Матьє',
         'group': u'МВ-51'},
        {'id': 2,
         'title': u'Операційні системи',
         'date': '21-03-2018',
         'teacher': u'Жорж Сіменон',
         'group': u'МВ-52'},
        {'id': 3,
         'title': u'Основи криптології',
         'date': '22-03-2018',
         'teacher': u'Жюль Верн',
         'group': u'МВ-53'},
    )
    return render(request, 'students/exams_list.html', {'exams': exams})


def exams_edit(request, eid):
    return HttpResponse('Exam %s Edit Form' % eid)


def exams_delete(request, eid):
    return HttpResponse('Exam %s Delete Form' % eid)
