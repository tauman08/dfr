from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return name


class ToDo(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
