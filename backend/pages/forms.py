# -*- coding: utf-8 -*-
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from captcha.fields import ReCaptchaField


class ContactFormHome(forms.Form):
    name = forms.CharField(
        label="Ваше имя*",
        widget=forms.TextInput(attrs={'class': 'input__contacts'})
    )

    email = forms.EmailField(
        label="E-mail*",
        widget=forms.EmailInput(attrs={'class': 'input__contacts'})
    )

    message = forms.CharField(
        label="Сообщение*",
        widget=forms.Textarea(attrs={'class': 'message__contacts'})
    )

    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'light', 'data-size': 'normal'})
    )
