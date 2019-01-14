# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

from ..models.student import Student
from ..models.group import Group


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
    if request.method == "POST":
        if request.POST.get('add_button') is not None:

            errors = {}

            # validate student data will go there
            data = {'middle_name': request.POST['middle_name'],
                    'notes': request.POST['notes']}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Імʼя є обовʼязковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обовʼязковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обовʼязковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обовʼязковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.POST.get('photo', '').strip()
            if photo:
                data['photo'] = photo

            if not errors:
                student = Student(**data)
                student.save()
                return HttpResponseRedirect(
                    u'%s?status_message=Студента успішно додано!' % reverse('home'))

            else:
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                u'%s?status_message=Додавання студента скасовано!' % reverse('home'))

    else:
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('students %s Edit Form' % sid)


# def students_attend(request, sid):
#    return HttpResponse('student %s Attend Form' % sid)  - поміняв на journal_attend


def students_delete(request, sid):
    return HttpResponse('student %s Delete Form' % sid)
