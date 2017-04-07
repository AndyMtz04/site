from django.contrib import admin
from .models import Project, About, FrontPage, FrontPageProject

#admin.site.register(Post)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(FrontPage)
admin.site.register((FrontPageProject))