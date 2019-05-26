from django.db import models
from django.urls import reverse
from PIL import Image
from django import forms
# from django.forms import ModelForm

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories_pics', default='default_cat_img.png')
    description = models.TextField(blank=True, max_length=10000)
    slug = models.SlugField(unique=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    @property
    def meals_by_cat(self):
        return Meal.objects.filter(category=self.pk)

    class Meta:
        verbose_name_plural = "categories"


class Meal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals_pics', default='default_meal_img.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)    # This defines how we can order Meals

    def get_absolute_url(self):
        return reverse('meal_details', args=[self.pk, self.slug])



