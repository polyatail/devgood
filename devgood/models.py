from django.db import models

class Developer(models.Model):
    user = models.ForeignKey(User)

    school = models.CharField(max_length=1024)
    skills = models.CharField(max_length=2048)
    portfolio_url = models.CharField(max_length=1024)
    about_me = models.CharField(max_length=2048)

class NPO(models.Model):
    user = models.ForeignKey(User)

    npo_name = models.CharField(max_length=1024)
    npo_url = models.CharField(max_length=1024)
    mission_short = models.CharField(max_length=1024)
    mission_long = models.CharField(max_length=2048)

class Project(models.Model):
    name = models.CharField(max_length=140)

    STATUSCHOICES = (0, "Created",
                     1, "Submitted",
                     2, "Matched",
                     3, "Completed",
                     4, "Cancelled-Matched",
                     5, "Cancelled-Unmatched")

    status = models.CharField(max_length=1, choices=STATUSCHOICES)
    requested_by = models.ForeignKey(User)
