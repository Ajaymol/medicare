from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='category')

    class Meta:
        ordering = ("name",)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse("ecommerceapp:doctors by category", args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Doctor(models.Model):
    name = models.CharField(max_length=550, unique=True)
    slug = models.SlugField(max_length=550, unique=True)
    available = models.BooleanField(default=True)
    charge = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='doctor')

    class Meta:
        ordering = ("name",)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def get_url(self):
        return reverse("ecommerceapp:doctorsDetails",args=[self.category.slug, self.slug])
    def get_urls(self):
        return reverse("ecommerceapp:doctorsDetail",args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
