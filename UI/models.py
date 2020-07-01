from django.db import models

# Create your models here.

DCC_CHOICES = (
    ('DC1','DC1'),
    ('DC2', 'DC2'),
    ('DC4','DC4'),
    ('DC8','DC8'),
    ('DC10','DC10'),
)

job_choices = (
    ('rundeck', 'rundeck'),
    ('splunk', 'splunk'),
    ('zabbix', 'zabbix')
)

class UserSqlData(models.Model):
    query = models.CharField(max_length=100,blank=False)
    dcc = models.CharField(max_length=6, choices=DCC_CHOICES, blank=False)
    environment = models.CharField(max_length =10,blank=False)
    server = models.CharField(max_length =10,blank=False)
    need_schedule = models.BooleanField()


class UserApiData(models.Model):
    api_url = models.URLField(blank=False)
    job = models.CharField(max_length=10, choices = job_choices,blank=False)
    need_schedule = models.BooleanField()


class UserSshData(models.Model):
    command = models.CharField(max_length=100,blank=False)
    job = models.CharField(max_length=10, choices=job_choices, blank=False)
    need_schedule = models.BooleanField()


