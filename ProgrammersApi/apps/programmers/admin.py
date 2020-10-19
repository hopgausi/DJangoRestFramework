from django.contrib import admin
from apps.programmers.models import Programmer, Company, Language

# Registering Models to be viewed in admin dashboard
admin.site.register(Programmer)
admin.site.register(Company)
admin.site.register(Language)
