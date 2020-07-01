from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from profile_page.models import profile_details,educations,projects,skills,about_details,professional_experience,social_profiles
from django.db import IntegrityError


# Create your views here.
def signup(request):
    print ('dhbdkcndkjnjkd---------------------------------')
    if request.method=='POST':
        fullname=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['pass']
        repeat_password=request.POST['repeat-pass']

        user=User.objects.create_user(username=username, email=email, password=password, first_name=fullname)
        print (user)
        user.save()
        details=profile_details.objects.create(username=username, About_me_Home='I am a passionate Cyber Security Expert from Bangalore')
        abt = about_details(username=details, Website='https://resumeaayush.herokuapp.com/', City='Bangalore', Birthday='24/01/1996', Age=24, Freelance='Available', Job_Title='QA-Cyber Security', Degree='Masters', Job_details='I am Responsible for performing Security testing on website, new deployments and internal network. R&D Member(Guild Team) for Penetration Testing and Security Audits' ,About_me_About='High inclination towards fancy technology with crazy innovative ideas to do things differently. With great taste of music, movies and sarcasm. IT professional with serious fitness goals', Email='aayush.bhrgv@gmail.com', MobileNumber=8602937010, Address='H-11 Kitiyani', Image='batman.jpg')
        edu = educations(username=details, degree_name='Bachelors of Engineering', institute_name='Medicaps Institute of Technology and Management, Indore', year_of_education='2014-2018', about_education='Student of Electronics and Instrumentation branch. Big time innovater in the feild.')
        skil = skills(username=details, skill_name='HTML', skill_profeciency=75)
        profx = professional_experience(username=details, designation='Cyber Security Expert', year_of_work='2018-Present', company_name='Evive, Bangalore', about_work='R&D Member for Penetration Testing and Security Audits, Responsible for performing Security testing on website, new deployments and internal network')
        soc = social_profiles(username=details, github='https://github.com/aayush860', facebook='https://www.facebook.com/profile.php?id=100009253032201', instagram='https://www.instagram.com/ayush23.24/', linkedin='https://www.linkedin.com/in/aayush-bhargava-5b627851/')

        #proj = projects(username=details, project_name='BE', institute_name='medicaps', year_of_education='2014-2018', about_education='Electronics')
        abt.save()
        skil.save()
        details.save()
        edu.save()
        profx.save()
        soc.save()

        return redirect('/signin/')
    else:
        if request.user.is_authenticated:
            return redirect('/signin/')
        return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/profile/'+username+'/')
        else:
            return render(request, 'signin.html')
    else:
        user=request.user.username
        if user!='':
            return redirect('/profile/'+user+'/')
        else:
            return render(request, 'signin.html')



