# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = (
        {'id': 1,
        'name': u'МВ-51',
        'leader': {'id': 1, 'name': u'Джон Сендвік'}},
        {'id': 2,
        'name': u'МВ-52',
        'leader': {'id': 2, 'name': u'Майкл Ліндсі'}},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('Group %s Edit Form' % gid)


def groups_delete(request, gid):
    return HttpResponse('Group %s Delete Form' % gid)
