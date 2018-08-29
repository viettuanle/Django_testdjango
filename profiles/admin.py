from django.contrib import admin

# Register your models here.
from profiles.models import MyUser

admin.site.register(MyUser)