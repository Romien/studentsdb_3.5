# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Exam(models.Model):

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"
        ordering = ['title']

    title = models.CharField(
        max_length=256, blank=False, verbose_name=u"Назва іспиту")
    date = models.DateTimeField(
        blank=False, verbose_name=u"Дата іспиту")
    teacher = models.CharField(
        max_length=256, blank=False, verbose_name=u"Викладач")
    exam_group = models.ForeignKey(
        'Group', verbose_name=u"Група", blank=False, null=True, on_delete=models.PROTECT)

    # def __str__(self):
    #     return '{} {}'.format(self.title, self.date)
    def __unicode__(self):
        return u"%s %s" % (self.title, self.date)
