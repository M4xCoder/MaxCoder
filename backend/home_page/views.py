from django.shortcuts import render


def home_page(request):
    pagename = 'MaxCoder'
    return render(request, 'home.html', {'pagename': pagename})
