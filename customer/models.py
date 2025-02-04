from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.core.validators import MinValueValidator,MaxValueValidator
from uuid import uuid4
from django.utils import timezone
from django.utils.timezone import localtime,timedelta
from django.urls import reverse
from secrets import token_urlsafe
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WishItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='wishlist')
    created=models.DateField(auto_now_add=True)


class BasketItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='basketlist')
    count=models.IntegerField(default=0)
    # size=models.ForeignKey('shop.Size',on_delete=models.CASCADE)
    # color=models.ForeignKey('shop.Color',on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()
    

class Review(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='reviews')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    comment=models.TextField()
    star_count=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created=models.DateField(auto_now_add=True)
    


class ResetPassword(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.token = self.token or token_urlsafe(50)
        return super().save(*args, **kwargs)

    def is_valid(self):
        not_used = not self.used
        not_expired = (localtime() - timedelta(days=1)) < self.created
        return not_used and not_expired
    
    def get_absolute_url(self):
        return reverse("customer:reset-password", kwargs={"token": self.token})
    

