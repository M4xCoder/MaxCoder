from django.shortcuts import render

def store_page(request):
    pagename = 'MaxCoder'
    return render(request, 'store/store.html', {'pagename': pagename})
