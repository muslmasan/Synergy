# from django.db import models
# from home.models import UserProfile
# # Create your models here.
# typeChoices = (
#     ("PART TIME", 'Part time'),
#     ("FULL TIME", "Full time"),
#     ("INTERNERSHIP", "Internership"),
# )


# class Job(models.Model):
#     title = models.CharField(max_length=256)
#     image = models.BinaryField(blank=True)
#     cover = models.BinaryField(blank=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     location = models.CharField(max_length=100)
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     type = models.CharField(
#         max_length=100,
#         choices=typeChoices,

#     )
