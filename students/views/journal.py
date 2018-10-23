# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def journal(request):
    # groups = (
    #     {'id': 1,
    #      'name': u'МВ-51',
    #      'leader': {'id': 1, 'name': u'Джон Сендвік'}},
    #     {'id': 2,
    #      'name': u'МВ-52',
    #      'leader': {'id': 2, 'name': u'Майкл Ліндсі'}},
    # )
    journal = (
        {'id': 1,
         'name': u'Фрімен Джанґо'},
        {'id': 2,
         'name': u"Креш Біллі"},
        {'id': 3,
         'name': u"Сліммі Джейкоб"}
    )
    return render(request, 'students/journal.html', {'journal': journal})


def journal_attend(request, sid):
    return HttpResponse('student %s Attend Form' % sid)
