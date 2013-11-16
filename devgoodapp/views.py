from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from models import Developer, NPO, Project

# Create your views here.

def npo_dashboard(request):
    if request.user.is_authenticated():
	npo = NPO.objects.get(user=request.user)
        projects = Project.objects.filter(requested_by=request.user)

        return render_to_response(
            "npo_dashboard.html",
            {"npo": npo.__dict__,
             "projects": projects}
        )
    else:
        return HttpResponse("You need to login")

def dev_dashboard(request):
    if request.user.is_authenticated():
        dev = Developer.objects.get(user=request.user)
        projects = Project.objects.filter(assigned_to=request.user)

        return render_to_response(
            "dev_dashboard.html",
            {"dev": dev.__dict__,
             "projects": projects}
        )
    else:
        return HttpResponse("You need to login")

def project_detail(request,requested_project_id):
    project = Project.objects.get(id=requested_project_id)
    return HttpResponse("requested project id is  %s." % project)
#    return render_to_response(
#	"project_detail.html", 
#	{"project": project.__dict__}
#    )
    
