from django.shortcuts import render

def shop_page(request):
    pagename = 'MaxJournal'
    return render(request, 'shop.html', {'pagename': pagename})
