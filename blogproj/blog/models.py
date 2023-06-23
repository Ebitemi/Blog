from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=80,default="")
    author = models.CharField(max_length=50,default="")
    content = models.TextField(default="")
    date_posted = models.DateField(default=timezone.now)
    media_file = models.FileField(blank=True,null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    
class Staff(models.Model):
    role = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    img_File = models.FileField(blank=True)
    facebook = models.CharField(max_length=50,default="")
    twitter = models.CharField(max_length=50,default="")
    linkedIn = models.CharField(max_length=50,default="")
    instagram = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.user.username

class ContactUs(models.Model):
    name =  models.CharField(max_length=10)
    email =  models.CharField(max_length=30)
    subject =  models.CharField(max_length=10)
    number =  models.CharField(max_length=11)
    message =  models.CharField(max_length=100)



# class WelcomeArea(models.Model):
#     heading = models.CharField(max_length=10)
#     text = models.CharField(max_length=30)
#     img = models.FileField(blank=True)


# class Opportunities(models.Model):
#     Category = models.ForeignKey(Categories, on_delete=models.CASCADE)


# class Bootcamps(models.Model):
#     title = models.CharField(max_length=30)
#     img = models.FileField(blank=True)
#     text = models.CharField(max_length=100)

class Login(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)

class Opportunity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OpportunityPost(models.Model):
    background = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=30, default="")
    content = models.CharField(max_length=100)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class InternshipPost(models.Model):
    background = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=100)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class JobPost(models.Model):
    background = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=100)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ScholarshipPost(models.Model):
    background = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=100)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Memes(models.Model):
    picture = models.FileField(null=True, blank=True)
    
    
class Jokes(models.Model):
    content = models.TextField(blank=True, default="")
    
class Event(models.Model):
    background = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title

