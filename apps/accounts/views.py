from django.shortcuts import render
from django.views.generic import View
from apps.accounts.models import LicenseBrickDesign


class ProfilePage(View):

    def get(self, request):
        pagename = 'MaxJournal'
        return render(request, 'profile.html', {'pagename': pagename})

class LicensePage(View):

    def get(self, request):
        pagename = 'MaxJournal'
        user = request.user
        return render(request, 'license.html', {'pagename': pagename, 'user': user})
