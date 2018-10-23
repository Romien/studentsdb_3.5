from django.db import models

# Create your models here.


class Group(models.Model):

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"
        ordering = ['title']

    title = models.CharField(
        max_length=256, blank=False, verbose_name=u"Назва")
    notes = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")
    leader = models.OneToOneField(
        'Student', verbose_name=u"Староста", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.leader:
            return '{} {} {}'.format(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '{}'.format(self.title,)
