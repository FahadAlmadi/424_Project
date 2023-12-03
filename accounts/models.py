from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from shop.models import Item
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required


class UserProfile(models.Model):
    name = models.CharField(_("الأسم"),max_length=200)
    email= models.EmailField(_("البريد الإلكتروني"),max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items_purchased = models.ManyToManyField(Item)

    def __str__(self):
           return self.user.username
       
       

