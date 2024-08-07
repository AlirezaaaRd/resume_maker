from django.contrib import admin

# Register your models here.

from app_resume.models import Resume , work_experience

admin.site.register(Resume)
admin.site.register(work_experience)