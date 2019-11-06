from django.shortcuts import render

def shop_page(request):
    pagename = 'MaxCoder'
    return render(request, 'shop/shop.html', {'pagename': pagename})
