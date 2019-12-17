from .forms import ContactFormHome
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def home_page(request):
    pagename = 'MaxCoder'

    if request.method == 'POST':
        form = ContactFormHome(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['pritvor69@bk.ru']

            try:
                send_mail(name, message, 'pritvor69@bk.ru', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'pages/home.html', {'pagename': pagename, 'form': form})
    else:
        # Заполняем форму
        form = ContactFormHome()
    # Отправляем форму на страницу
    return render(request, 'pages/home.html', {'pagename': pagename, 'form': form})
