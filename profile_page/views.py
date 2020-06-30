from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from profile_page.models import profile_details,educations,projects,skills,about_details,professional_experience,social_profiles,interests
from django.http import HttpResponse

import json
# Create your views here.

def autocompleteModel(request):
    mimetype = 'application/json'
    if request.is_ajax():
        q = request.GET.get('q', '').capitalize()
        search_qs = User.objects.filter(first_name__icontains=q)
        results = []
        username = []
        for r in search_qs:
            keyx = profile_details.objects.get(username=r.username)
            details = about_details.objects.get(username=keyx)
            results.append(str(r.first_name)+' '+str(r.last_name)+' ,'+str(details.Job_Title))
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
        skilx = skills.objects.all().filter(username=dataa)
        about_det = about_details.objects.all().filter(username=dataa)
        educationn = educations.objects.all().filter(username=dataa)
        professional = professional_experience.objects.all().filter(username=dataa)
        social = social_profiles.objects.all().filter(username=dataa)
        interest = interests.objects.all().filter(username=dataa)
        size=len(skilx)//2
        return render(request, 'profilepage.html', {'size':size  ,'interest':interest,'social':social[0] ,'login_det':login_det, 'dataa':dataa, 'skilx':skilx, 'about_det':about_det[0], 'educationn':educationn, 'professional':professional})
    else:
        return redirect('/signin/')



def logout(request):
    auth.logout(request)
    return redirect('/signin/')
