from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug


def pre_save_produkt_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.title, reversed=True))
        instance.slug = slug


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split(".")[1]
    return '{0}/{1}'.format(instance.slug, filename)


class Section(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title


pre_save.connect(pre_save_category_slug, sender=Category)
pre_save.connect(pre_save_produkt_slug, sender=Product)
