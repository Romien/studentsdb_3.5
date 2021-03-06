"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


"""
from .settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from students import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # Students urls
    url(r'^$', views.students_list, name='home'),
    url(r'^students/add/$', views.students_add, name='students_add'),
    url(r'^students/(?P<sid>[0-9]+)/edit/$',
        views.students_edit, name='students_edit'),

    # url(r'^students/(?P<sid>[0-9]+)/attend/$',
    #     views.students_attend, name='students_attend'),
    url(r'^students/(?P<sid>[0-9]+)/delete/$',
        views.students_delete, name='students_delete'),


    # Groups urls
    url(r'^groups/$', views.groups_list, name='groups_list'),
    url(r'^groups/add/$', views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>[0-9]+)/edit/$',
        views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>[0-9]+)/delete/$',
        views.groups_delete, name='groups_delete'),

    # Journal urls
    url(r'^journal/$', views.journal, name='journal'),
    url(r'^journal/(?P<sid>[0-9]+)/attend/$',
        views.journal_attend, name='journal_attend'),

    # Exams urls
    url(r'^exams/$', views.exams_list, name='exams_list'),
    url(r'^exams/add/$', views.exams_add, name='exams_add'),
    url(r'^exams/(?P<eid>[0-9]+)/edit/$',
        views.exams_edit, name='exams_edit'),
    url(r'^exams/(?P<eid>[0-9]+)/delete/$',
        views.exams_delete, name='exams_delete'),


    url(r'^admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
