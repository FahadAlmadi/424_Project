
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Item(models.Model):
       name = models.CharField(_("الأسم"),max_length=255)
       description = models.TextField(_("التفاصيل"),)
       price = models.DecimalField(_("السعر"),max_digits=10, decimal_places=2)
       image =models.ImageField(_("الصورة"),upload_to='images')

       def __str__(self):
           return self.name


       
       