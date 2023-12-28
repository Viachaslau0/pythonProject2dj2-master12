from django.db import models
from django.db.models import CharField
from autoslug import AutoSlugField
from django.utils.text import slugify as django_slugify
from transliterate import translit



def russian_slugify(value):
    value = translit(value, 'ru', reversed=True)
    return django_slugify(value)


class Category(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    desc = models.TextField(max_length=4096)
    slug = AutoSlugField(populate_from='name', unique=True,editable=True,slugify=russian_slugify)

    class Meta:
        ordering = ['name']

    def __str__(self) -> CharField:
        return self.name

    def save(self, *args, **kwargs):
        # Вы можете добавить здесь любую логику, которую хотите выполнить при сохранении.
        super().save(*args, **kwargs)




class FoodItem(models.Model):

    price = models.FloatField()
    name = models.CharField(max_length=32, null=False, blank=False)
    desc = models.TextField(max_length=4096, null=False, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True,editable=True,slugify=russian_slugify)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self) -> CharField:
        return self.name

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)



