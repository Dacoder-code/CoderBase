from django.db import models

# Create your models here.


class Allcourse(models.Model):
    CourseName = models.CharField(max_length=200)
    InstructorName = models.CharField(max_length=200)

    def __str__(self):
        return self.CourseName


class Details(models.Model):
    course = models.ForeignKey(Allcourse, on_delete=models.CASCADE)
    SelfPaced = models.CharField(max_length=700)
    InstructorLead = models.CharField(max_length=700)

    def __str__(self):
        return self.SelfPaced
