from django.db import models

# Create your models here.
class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    keywords = models.CharField(blank=True, max_length=200)
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=300)
    company= models.CharField(max_length=50)
    adress = models.CharField(blank=True,max_length=50)
    phone = models.CharField(blank=True,max_length=10)
    fax = models.CharField(blank=True,max_length=10)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(max_length=20)
    semtepemail = models.CharField(max_length=20)
    smtppasword = models.CharField(max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/',)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    aboutus = models.TextField(blank=True,)
    contact = models.TextField(blank=True,)
    references = models.TextField(blank=True,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)
    def __str__(self):
            return self.title