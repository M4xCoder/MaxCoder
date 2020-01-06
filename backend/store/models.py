from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
import random


def pre_save_key_email(sender, instance, *args, **kwargs):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for n in range(4):
        for i in range(4):
            password += random.choice(chars)
        password += '-'
    print(password)
    instance.key = password[:-1]
    if instance.user.email:
        instance.email = instance.user.email


def pre_save_url(sender, instance, *args, **kwargs):
    if not instance.url:
        url = slugify(translit(instance.name, reversed=True))
        instance.url = url


def image_folder(instance, filename):
    filename = instance.url + '.' + filename.split(".")[1]
    return '{0}/{1}'.format(instance.url, filename)


class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT)
    description = models.TextField()
    logo = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.SlugField(blank=True)
    platform = models.ForeignKey('Platform', on_delete=models.PROTECT, default='')
    images = models.ForeignKey('Images', on_delete=models.PROTECT, default='')

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    url = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class License(models.Model):
    app = models.ForeignKey(App, blank=True, on_delete=models.PROTECT, verbose_name='App')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='User')
    key = models.SlugField(max_length=19, blank=True, verbose_name='Key')
    id_computer = models.CharField(max_length=250, blank=True, verbose_name='Computer name')
    id_program = models.CharField(max_length=8, blank=True, verbose_name='ID program')
    email = models.EmailField(blank=True, default='xxx@xxx.xx', verbose_name='E-mail')

    def __str__(self):
        return self.email


pre_save.connect(pre_save_url, sender=Category)
pre_save.connect(pre_save_url, sender=App)
pre_save.connect(pre_save_url, sender=Images)
pre_save.connect(pre_save_key_email, sender=License)
