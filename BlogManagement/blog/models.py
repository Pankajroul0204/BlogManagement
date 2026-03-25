from django.db import models
from django.conf import settings

class Contact(models.Model):
    SERVICE_OPTIONS = [
        (0, 'Consulting'),
        (1, 'Development'),
        (2, 'Marketing'),
        (3, 'Support')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    message = models.TextField()
    service = models.CharField(max_length=20, choices=SERVICE_OPTIONS)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    active = models.BooleanField(max_length=1,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
class Blog(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_desc = models.TextField()
    description = models.TextField()
    images = models.ImageField(upload_to='blog_images/')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.short_desc

class Team(models.Model):
        name = models.CharField(max_length=50)
        designation = models.CharField(max_length=50)
        short_desc = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        list_filter = [name,designation,created_at]

        def __str__(self):
            return self.name