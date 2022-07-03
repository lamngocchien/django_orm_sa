# db/models.py
from django.db import models
from manage import init_django

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Record(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = 'Record'

    ac_reg = models.CharField(max_length=64, default='')
    type = models.CharField(max_length=64, default='')
    arr = models.CharField(max_length=64, default='')
    dep = models.CharField(max_length=64, default='')
    route = models.CharField(max_length=64, default='')
    date = models.DateField(blank=True, null=True)
    eta = models.DateTimeField(blank=True,null=True)
    etd = models.DateTimeField(blank=True, null=True)
    time_eta = models.CharField(max_length=64, default='')
    time_etd = models.CharField(max_length=64, default='')
    enable = models.BooleanField(default=True)

    # transist = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return '%s/%s/%s' % (self.ac_reg, self.time_eta, self.type)