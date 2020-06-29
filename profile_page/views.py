from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from profile_page.models import profile_details,educations,skills
from django.http import HttpResponse

import json
# Create your views here.

def autocompleteModel(request):
    print ('-------------------------------')
    mimetype = 'application/json'
    if request.is_ajax():
        q = request.GET.get('q', '').capitalize()
        search_qs = User.objects.filter(first_name__icontains=q)
        results = []
        username = []
        for r in search_qs:
            results.append(r.first_name)
            username.append(r.username)
        results=results[:3]  
        username=username[:3] 
        the_data = json.dumps({
        'results': results,
        'username': username
        })
        return HttpResponse(the_data, mimetype)

    else:
        data = 'fail'

    
    return HttpResponse(data, mimetype)



#request.user.username
def profile(request,username):
    if request.user.is_authenticated:
        login_det = User.objects.get(username=username)
        dataa = profile_details.objects.get(username=username)
        print ('***********************************',dataa)
        educationn = educations.objects.all().filter(username=dataa)
        print ('***********************************',educationn)
        return render(request, 'profilepage.html', {'login_det':login_det, 'dataa':dataa, 'educationn':educationn})
    else:
        return redirect('/signin/')



def logout(request):
    print ('------------------------------++++++++++++++++++++++')
    auth.logout(request)
    return redirect('/signin/')




'''
def edit_info(request):
    if request.method=='POST' and request.user.is_authenticated:
        Birthday=request.POST['dob']
        Age=request.POST['age']
        Job_Title=request.POST['jtitle']
        About_me_Home=request.POST['aboutme1']
        About_me_About=request.POST['aboutme2']
        Email=request.POST['email']
        MobileNumber=request.POST['mobile']

        degree_name=request.POST['degree_name']
        institute_name=request.POST['institute_name']
        year_of_education=request.POST['year_of_education']
        about_education=request.POST['about_education']
        
        dataa=request.POST['payload']
        #details=profile_details.objects.filter(username=request.user.username).update(Birthday=Birthday, Age=Age, Job_Title=Job_Title, About_me_Home=About_me_Home, About_me_About=About_me_About, Email=Email, MobileNumber=MobileNumber)
        #dataa = profile_details.objects.get(username=request.user.username)
        for_key=profile_details.objects.get(username=request.user.username)
        dataa = json.loads(dataa)
        dataa = dataa['data'][2:]
        for i in dataa:
            skix = skills.objects.create(username=for_key, skill_name=i[0], skill_profeciency=i[1])
            skix.save()
        #educationn = educations.objects.create(username=dataa, degree_name='BEX', institute_name='medicaps', year_of_education='2014-2018', about_education='Electronics')
        return redirect('/signin/')

    else:
        if request.user.is_authenticated:
            dataa = profile_details.objects.get(username=request.user.username)
            skilx = skills.objects.all().filter(username=dataa)
            return render(request, 'editing_information.html', {'dataa':dataa, 'skilx':skilx})
        else:
            return redirect('/signin/')    
'''