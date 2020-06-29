from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from profile_page.models import profile_details,educations,skills,about_details,professional_experience,social_profiles,interests
from django.http import HttpResponse
import json
# Create your views here.

def edit_info(request):
    if request.user.is_authenticated:
        login_det = User.objects.get(username=request.user.username)
        dataa = profile_details.objects.get(username=request.user.username)
        skilx = skills.objects.all().filter(username=dataa)
        about_det = about_details.objects.all().filter(username=dataa)
        educationn = educations.objects.all().filter(username=dataa)
        professional = professional_experience.objects.all().filter(username=dataa)
        social = social_profiles.objects.all().filter(username=dataa)
        interest = interests.objects.all().filter(username=dataa)
        return render(request, 'EditInfo.html', {'interest':interest,'social':social[0] ,'login_det':login_det, 'dataa':dataa, 'skilx':skilx, 'about_det':about_det[0], 'educationn':educationn, 'professional':professional})
    else:
        return redirect('/signin/')



def update_home(request):
    if request.method=='POST' and request.user.is_authenticated:        
        dataa = request.POST['About_me_Home']
        print (dataa)
        key = profile_details.objects.get(username=request.user.username)
        details=profile_details.objects.filter(username=key).update(About_me_Home=dataa)
    return redirect('/edit_info/')


def update_about(request):
    if request.method=='POST' and request.user.is_authenticated:   
        Job_Title = request.POST['Job_Title']
        Job_details = request.POST['Job_details']
        About_me_About = request.POST['About_me_About']
        Degree = request.POST['Degree']
        Birthday = request.POST['Birthday']
        Freelance = request.POST['Freelance']
        Age = request.POST['Age']
        MobileNumber = request.POST['MobileNumber']
        City = request.POST['City']
        Website = request.POST['Website']
        key = profile_details.objects.get(username=request.user.username)
        details = about_details.objects.filter(username=key).update(Job_Title=Job_Title, Job_details=Job_details, About_me_About=About_me_About, Degree=Degree, Birthday=Birthday, Freelance=Freelance, Age=Age, MobileNumber=MobileNumber, City=City, Website=Website)
        #details=profile_details.objects.filter(username=key).update(About_me_About=dataa)
    return redirect('/edit_info/#about')


def update_skills(request):
    if request.method=='POST' and request.user.is_authenticated:        
        dataa=request.POST['payload']
        for_key=profile_details.objects.get(username=request.user.username)
        dataa = json.loads(dataa)
        dataa = dataa['data'][2:]
        for i in dataa:
            skix = skills.objects.create(username=for_key, skill_name=i[0], skill_profeciency=i[1])
            skix.save()
    return redirect('/edit_info/#about')

def update_education(request):
    if request.method=='POST' and request.user.is_authenticated:        
        try:
            dataa = request.POST['payload']
            for_key=profile_details.objects.get(username=request.user.username)
            dataa = json.loads(dataa)
            dataa = dataa['data'][2:]
            for i in dataa:
                educ = educations.objects.create(username=for_key, degree_name=i[0], year_of_education=i[1], institute_name=i[2], about_education=i[3])
                educ.save()
            return redirect('/edit_info/#resume')    
        except:
            degree_name = request.POST['degree_name']
            year_of_education = request.POST['year_of_education']
            institute_name = request.POST['institute_name']
            about_education = request.POST['about_education']
            idd = request.POST['id']
            print ('****************************' ,idd)
            key = profile_details.objects.get(username=request.user.username)
            details = educations.objects.filter(id=idd).update(degree_name=degree_name, year_of_education=year_of_education, institute_name=institute_name, about_education=about_education)
            return redirect('/edit_info/#resume')    


def update_profession(request):
    if request.method=='POST' and request.user.is_authenticated:        
        try:
            dataa = request.POST['payload']
            for_key=profile_details.objects.get(username=request.user.username)
            dataa = json.loads(dataa)
            dataa = dataa['data'][2:]
            for i in dataa:
                proff = professional_experience.objects.create(username=for_key, designation=i[0], year_of_work=i[1], company_name=i[2], about_work=i[3])
                proff.save()
            return redirect('/edit_info/#resume')    
        except:
            designation = request.POST['designation']
            year_of_work = request.POST['year_of_work']
            company_name = request.POST['company_name']
            about_work = request.POST['about_work']
            idd = request.POST['id']
            print ('****************************' ,idd)
            key = profile_details.objects.get(username=request.user.username)
            details = professional_experience.objects.filter(id=idd).update(designation=designation, year_of_work=year_of_work, company_name=company_name, about_work=about_work)
            return redirect('/edit_info/#resume')    


def update_interest(request):
    if request.method=='POST' and request.user.is_authenticated:  
        dataa = request.POST['payload']
        for_key=profile_details.objects.get(username=request.user.username)
        dataa = json.loads(dataa)
        dataa = dataa['data'][2:]
        for i in dataa:
            proff = interests.objects.create(username=for_key, interest=i[0])
            proff.save()
        return redirect('/edit_info/#about')    

def update_social(request):
    if request.method=='POST' and request.user.is_authenticated:        
        github = request.POST['github']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        key = profile_details.objects.get(username=request.user.username)
        details = social_profiles.objects.filter(username=key).update(github=github, facebook=facebook, instagram=instagram, linkedin=linkedin)
    return redirect('/edit_info/')