from django.contrib import admin

# Register your models here.
from .models import User , Patients, Doctor

admin.site.register(User)
admin.site.register(Patients)
admin.site.register(Doctor)
