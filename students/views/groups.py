# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Group


def groups_list(request):
    groups = Group.objects.all()

    order = request.GET.get('order_by', '')
    if order in ('id', 'title', 'leader'):
        groups = groups.order_by(order)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    paginator = Paginator(groups, 3)

    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('Group %s Edit Form' % gid)


def groups_delete(request, gid):
    return HttpResponse('Group %s Delete Form' % gid)
