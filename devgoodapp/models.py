from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.ForeignKey(User)

    school = models.CharField(max_length=1024, blank=True)
    skills = models.CharField(max_length=2048, blank=True)
    portfolio_url = models.CharField(max_length=1024, blank=True)
    about_me = models.CharField(max_length=2048, blank=True)

class NPO(models.Model):
    user = models.ForeignKey(User)

    npo_name = models.CharField(max_length=1024, blank=True)
    npo_url = models.CharField(max_length=1024, blank=True)
    mission_short = models.CharField(max_length=1024, blank=True)
    mission_long = models.CharField(max_length=2048, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=140)

    STATUSCHOICES = (("0", "Created"),
                     ("1", "Submitted"),
                     ("2", "Matched"),
                     ("3", "Completed"),
                     ("4", "Cancelled-Matched"),
                     ("5", "Cancelled-Unmatched"))

    status = models.CharField(max_length=1, choices=STATUSCHOICES)
    requested_by = models.ForeignKey(User, related_name="+")
    assigned_to = models.ForeignKey(User, related_name="+")
    project_short = models.CharField(max_length=1024, blank=True)
    project_long = models.CharField(max_length=2048, blank=True)

    PROJECTTYPE = (("0", "Entire Website"),
                   ("1", "Content Modification"),
                   ("2", "Redesign"))

    project_type = models.CharField(max_length=1, choices=PROJECTTYPE)
