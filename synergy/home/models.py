from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices = (
    ("MALE", "male"),
    ("FEMALE", "female"),
)


class UserProfile(AbstractUser):
    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    image = models.BinaryField(blank=True, null=True,editable=True)
    cover = models.BinaryField(blank=True, null=True, editable=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(
        max_length=20,
        choices=gender_choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
