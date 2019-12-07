from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.

class Class(models.Model):
    grade = models.IntegerField(default=datetime.now().year + 3)
    major = models.CharField(max_length=100)
    class_number = models.CharField(max_length=50)


class LectureUser(AbstractUser):
    student_id = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    email = models.EmailField(_('email address'))
    USERNAME_FIELD = 'student_id'
    objects = CustomUserManager()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.student_id) + " " + self.username


