from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices = (
    ("MALE", "male"),
    ("FEMALE", "female"),
)


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to= 'profile_images/',blank=True)
    cover = models.ImageField(upload_to='profile_covers/',blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(
        max_length=20,
        choices=gender_choices,
        blank= True,
    )

    def __str__(self):
        return self.username