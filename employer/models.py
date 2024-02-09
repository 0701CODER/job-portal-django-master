import datetime
import humanize

from PIL import Image
from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels

from portal.models import  User, Category


class Company(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    co_introduction = models.TextField()
    logo = models.ImageField(default='default.png', upload_to='co-logo')
    link  = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)

        img = Image.open(self.logo.path)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    experience_choices = (
        ('no-matter','No matter'),
        ('1-3', 'one to 3 years'),
        ('3-6', 'three to 6 years'),
        ('+6', 'more than 6 years'),
    )
    experience = models.CharField(max_length=80, choices=experience_choices)
    salary_choices = (
        ('agreement ', 'consensual'),
        ('from 3', 'from 3 million'),
        ('from 5', 'from 5 million'),
        ('from 8', 'from 8 million'),
        ('from 10', 'from 10 million'),
        ('from 12', 'from 12 million'),
        ('from 15', 'from 15 million'),
    )
    salary = models.CharField(
        max_length=80, choices=salary_choices
    )
    cooperation_choices = (
        ('full-time', 'full-time'),
        ('part-time', 'part-time'),
        ('remote', 'remote'),
        ('internship', 'internship'),
    )
    cooperation_type = models.CharField(
        max_length=80, choices=cooperation_choices
    )
    job_description = models.TextField()
    skills_required = models.CharField(max_length=80)
    military_choices = (
        ('no-matter', 'no-matter'),
        ('end', 'end of service'),
    )
    military_service = models.CharField(
        max_length=80, choices=military_choices
    )
    degree_choices = (
        ('no-matter', 'no-matter'),
        ('diploma', 'diploma'),
        ('bachelor', 'bachelor'),
    )
    degree = models.CharField(max_length=80, choices=degree_choices)
    gender_choices = (
        ('Male', 'men'),
        ('Female', 'women'),
        ('not-matter','not-matter'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices)

    def __str__(self):
        return self.title
    
    
class JobRequests(models.Model):
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume_url = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    hired = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.jobseeker} requested on {self.job}'
    
    def save(self, *args, **kwargs):
        super(JobRequests, self).save(*args, **kwargs)