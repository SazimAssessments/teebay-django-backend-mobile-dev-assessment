from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    firebase_console_manager_token = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
