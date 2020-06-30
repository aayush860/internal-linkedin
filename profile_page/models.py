from django.db import models

# Create your models here.
class profile_details(models.Model):
    username = models.TextField()
    About_me_Home = models.TextField()
    def __str__(self):
            return self.username

class about_details(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    Job_Title = models.CharField(max_length=32)
    Job_details = models.TextField()
    About_me_About = models.TextField()
    Degree = models.CharField(max_length=32)
    Birthday = models.CharField(max_length=16)
    Freelance = models.CharField(max_length=32)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=256)
    MobileNumber = models.CharField(max_length=10)
    City = models.CharField(max_length=32)
    Website = models.TextField()
    Address = models.TextField()
    Image = models.ImageField(upload_to='media/')

class educations(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    degree_name = models.TextField()
    institute_name = models.TextField()
    year_of_education = models.TextField()
    about_education = models.TextField()


class skills(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=56)
    skill_profeciency = models.IntegerField()


class professional_experience(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    designation = models.CharField(max_length=56)
    year_of_work = models.CharField(max_length=56)
    company_name = models.CharField(max_length=56)
    about_work = models.TextField()


class interests(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    interest = models.CharField(max_length=32)


class social_profiles(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    github = models.TextField()
    facebook = models.TextField()
    instagram = models.TextField()
    linkedin = models.TextField()


class achivement(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    name_of_achivement = models.CharField(max_length=56)
    year = models.CharField(max_length=32)
    about_achivement = models.TextField()


class certificate(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    name_of_certificate = models.CharField(max_length=56)
    year_achived = models.CharField(max_length=32)
    about_certificate = models.TextField()
    certificate_link = models.TextField()

class projects(models.Model):
    username = models.ForeignKey(profile_details, on_delete=models.CASCADE)
    name_of_project = models.CharField(max_length=56)
    year_made = models.CharField(max_length=32)
    about_project = models.TextField()
    project_link = models.TextField()