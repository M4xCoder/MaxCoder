from django.shortcuts import render
from django.views.generic import View
from .models import LicenseBrickDesign


class ProfilePage(View):

    def get(self, request):
        pagename = 'MaxCoder'
        return render(request, 'profile.html', {'pagename': pagename})

class LicensePage(View):

    def get(self, request):
        pagename = 'MaxCoder'
        user = request.user
        return render(request, 'license.html', {'pagename': pagename, 'user': user})
