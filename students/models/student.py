from django.db import models

# Create your models here.


class Student(models.Model):

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"
        ordering = ['last_name']

    first_name = models.CharField(
        max_length=256, blank=False, verbose_name=u"Ім'я")
    last_name = models.CharField(
        max_length=256, blank=False, verbose_name=u"Прізвище")
    middle_name = models.CharField(
        max_length=256, blank=True, verbose_name=u"По-батькові", default='')
    birthday = models.DateField(
        blank=False, verbose_name=u"Дата народження", null=True)
    photo = models.ImageField(blank=True, verbose_name=u"Фото", null=True)
    ticket = models.CharField(
        max_length=256, blank=False, verbose_name=u"Білет")
    student_group = models.ForeignKey(
        'Group', verbose_name=u"Група", blank=False, null=True, on_delete=models.PROTECT)
    notes = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)