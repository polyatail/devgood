from django.contrib import admin

# Register your models here.
from models import Developer, NPO, Project

admin.site.register(Developer)
admin.site.register(NPO)
admin.site.register(Project)
