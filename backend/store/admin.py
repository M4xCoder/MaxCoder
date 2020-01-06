from django.contrib import admin
from .models import Category, App, Platform, Images, License

admin.site.register(Category)
admin.site.register(App)
admin.site.register(Platform)
admin.site.register(Images)
admin.site.register(License)
