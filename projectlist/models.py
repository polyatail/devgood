from django.db import models

# Create your models here.
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
