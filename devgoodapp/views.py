from django.shortcuts import render, render_to_response
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

