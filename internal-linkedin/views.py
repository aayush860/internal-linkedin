from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from profile_page.models import profile_details,educations,projects,skills,about_details,professional_experience,social_profiles
from django.db import IntegrityError

def redirectx(request):
    if isinstance(request, str) is False and request.method=='GET' and profile_details.objects.filter(username=request.user.username).exists() is False:
        details=profile_details.objects.create(username=request.user.username, About_me_Home='I am a passionate Cyber Security Expert from Bangalore')
        abt = about_details(username=details, Website='https://resumeaayush.herokuapp.com/', City='Bangalore', Birthday='24/01/1996', Age=24, Freelance='Available', Job_Title='QA-Cyber Security', Degree='Masters', Job_details='I am Responsible for performing Security testing on website, new deployments and internal network. R&D Member(Guild Team) for Penetration Testing and Security Audits' ,About_me_About='High inclination towards fancy technology with crazy innovative ideas to do things differently. With great taste of music, movies and sarcasm. IT professional with serious fitness goals', Email='aayush.bhrgv@gmail.com', MobileNumber=8602937010)
        edu = educations(username=details, degree_name='B.E.', institute_name='Medicaps Institute of Technology and Management', year_of_education='2014-2018', about_education='Electronics andInstrumentation')
        skil = skills(username=details, skill_name='HTML', skill_profeciency=75)
        profx = professional_experience(username=details, designation='Cyber Security Expert', year_of_work='2018-Present', company_name='Evive', about_work='R&D Member for Penetration Testing and Security Audits, Responsible for performing Security testing on website, new deployments and internal network')
        soc = social_profiles(username=details, github='https://github.com/aayush860', facebook='https://www.facebook.com/profile.php?id=100009253032201', instagram='https://www.instagram.com/ayush23.24/', linkedin='https://www.linkedin.com/in/aayush-bhargava-5b627851/')
        #proj = projects(username=details, project_name='BE', institute_name='medicaps', year_of_education='2014-2018', about_education='Electronics')
        abt.save()
        skil.save()
        details.save()
        edu.save()
        profx.save()
        soc.save()
        return redirect('/signin')
    else:
        return redirect('/signin')