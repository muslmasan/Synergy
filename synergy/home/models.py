from django.db import models

gender_choices = (
    ("MALE","male"),
    ("FEMALE","female"),
)


class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    cover = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(
        max_length=20,
        choices= gender_choices,
    )

    

    
