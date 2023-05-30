from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.CharField(max_length=100)
    slug = models.TextField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.TextField()

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField(null=True)
    url = models.URLField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    slug = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    slug = models.TextField(unique=True)

    def __str__(self):
        return self.name
STOCK = (('In stock', 'In stock'),('Out of stock','Out of stock'))
LABELS = (('Hot','Hot'),('New','New'),('Sale','Sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    specification = RichTextField()
    slug = models.TextField(unique=True)
    stock = models.CharField(max_length=100,choices=STOCK)
    label = models.CharField(max_length=100,choices=LABELS, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.product.name

class ProductReview(models.Model):
    username=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    comment=models.TextField()
    star=models.IntegerField()
    date=models.CharField(max_length=100)
    slug=models.TextField(default='Product')

    def __str__(self):
        return self.username

class Cart(models.Model):
    username=models.CharField(max_length=200)
    slug=models.TextField()
    quantity=models.IntegerField(default=1)
    total=models.IntegerField()
    checkout=models.BooleanField(default=False)
    items=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
