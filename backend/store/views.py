from django.shortcuts import render

def store_page(request):
    pagename = 'MaxCoder'
    return render(request, 'store/store.html', {'pagename': pagename})

def brick_designer_page(request):
    pagename = 'MaxCoder'
    return render(request, 'store/brick_designer.html', {'pagename': pagename})