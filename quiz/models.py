from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=7)

SCHOOL_CHOICES = (
    (None, 'Select SCHOOL'),
    ('SEET', 'SEET'),
    ('SAAT', 'SAAT'),
    ('SET', 'SET'),
    ('SEMS', 'SEMS'),
    ('SPS', 'SPS'),
    ('SOC', 'SOC'),
    ('SOS', 'SOS')
)
LEVEL_CHOICES = (
    (None, 'Select LEVEL'),
    ('100', '100'),
    ('200', '200'),
    ('300', '300'),
    ('400', '400'),
    ('500', '500'),
)

class Database(models.Model):
    school = models.CharField(max_length=100, null=True, choices = SCHOOL_CHOICES)
    level = models.CharField(max_length=100, null=True, choices = LEVEL_CHOICES)
    course = models.CharField(max_length=7, null=True)

    question = models.CharField(max_length=10000)

    optionA = models.CharField(default=None, max_length=500)
    optionB = models.CharField(default=None, max_length=500)
    optionC = models.CharField(default=None, max_length=500)
    optionD = models.CharField(default=None, max_length=500)

    answer = models.CharField(max_length=1)
    workings = models.TextField(null=True)

    def __str__(self):
        return f"{self.question} - {self.level} level - {self.course} "

