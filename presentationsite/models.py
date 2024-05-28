from django.db import models

class EmailModel(models.Model):
    email = models.EmailField(unique=True,blank=False)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()
    description = models.TextField()
    essence = models.TextField()
    slogan = models.CharField(max_length=255)
    url = models.URLField()
    industry = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Media(models.Model):
    media = models.FileField(upload_to='media/')
    thumbnail_url = models.URLField()
    media_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Campaign(models.Model):
    customer = models.ForeignKey(Customer, related_name='campaigns', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100)
    thumbnail_url = models.URLField()
    media_url = models.URLField()
    launched_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
