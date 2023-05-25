from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=12)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.phoneNumber} - {self.user.email} - {self.address}"   

class Skill(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, tasks=None):
        skill = cls(name=name)
        skill.save()
        if tasks:
            for task in tasks:
                Task.create(skill=name,description=task)
        return skill

class EmploymentHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class EducationHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.degree

class Qualification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)

    def __str__(self): 
        return self.qualification





class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
