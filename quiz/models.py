from django.db import models
from accounts.models import User


LEVEL_CHOICES = (
    (None, 'Select LEVEL'),
    ('100', '100'),
    ('200', '200'),
    ('300', '300'),
    ('400', '400'),
    ('500', '500'),
    ('600', '600'),
    ('700', '700'),
)


class MyLevel(models.Model):
    name = models.CharField(max_length=7, null=True, blank=True, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        return self.name[0:20]

class MyCourse(models.Model):
    level = models.ForeignKey(MyLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=7, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name[0:20]

class Question(models.Model):
    course = models.ForeignKey(MyCourse, default="", on_delete=models.CASCADE)
    
    question = models.TextField(default=None)

    optionA = models.TextField(default=None)
    optionB = models.TextField(default=None)
    optionC = models.TextField(default=None)
    optionD = models.TextField(default=None)

    answer = models.CharField(max_length=1)
    workings = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.course} - {self.question[0:20]} ..."

class Database(models.Model):
    level = models.CharField(max_length=100, null=True, choices=LEVEL_CHOICES)
    course = models.CharField(max_length=7, null=True)
    
    question = models.TextField(default=None)

    optionA = models.TextField(default=None)
    optionB = models.TextField(default=None)
    optionC = models.TextField(default=None)
    optionD = models.TextField(default=None)

    answer = models.CharField(max_length=1)
    workings = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.question[0:20]} level - {self.course} "

class AccountSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
