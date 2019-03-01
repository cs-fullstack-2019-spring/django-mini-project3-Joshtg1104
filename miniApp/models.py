from django.db import models
from django.utils import timezone


# Create your models here.

class TeacherTimeModel(models.Model):
    teacher_name = models.CharField(max_length=50, default="")
    school_name = models.CharField(max_length=100, default="")
    subject_teaching = models.CharField(max_length=100, default="")
    daily_hours_taught = models.IntegerField(default=1)
    date_of_work = models.DateField()
    date_of_entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.teacher_name
