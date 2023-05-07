from django.db import models
from django.contrib.auth.models import User
from django.utils.regex_helper import walk_to_end
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=255)
    
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





class Task(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    @classmethod
    def create(cls, skill, description):
        task = cls(skill=skill, description=description)
        task.save()
        return task
    def __str__(self):
        return self.skill.name




class Employment(models.Model):
    title = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class EducationHistory(models.Model):
    degree = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.degree

class Qualification(models.Model):
    qualification = models.CharField(max_length=255)

    def __str__(self): 
        return self.qualification


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=12)
    email = models.EmailField(max_length=255)
    qualifications = models.ManyToManyField('Qualification',
                                            related_name='profiles')
    skills = models.ManyToManyField('Skill', related_name='profiles')
    employments = models.ManyToManyField('Employment', related_name='profiles')
    education_history = models.ManyToManyField('EducationHistory', related_name='profiles')

    def __str__(self):
        return f"{self.user.username} - {self.phoneNumber} - {self.user.email} - {self.address}"   



class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
