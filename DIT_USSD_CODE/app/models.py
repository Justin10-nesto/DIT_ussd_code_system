from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    email = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    index_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Student"
        db_table = "Student"

class UserSelection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    value = models.BigIntegerField(null=True)

    def __str__(self):
        return self.student.email

    class Meta:
        verbose_name = "User Selection"
        db_table = "User Selection"
