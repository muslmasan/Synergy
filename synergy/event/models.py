# from django.db import models
# from home.models import UserProfile

# typeChoices = (
#     ("PART TIME",'Part time'),
#     ("FULL TIME", "Full time"),
#     ("INTERNERSHIP","Internership"),
# )

# class Event(models.Model):
#     title = models.CharField(max_length=256)
#     cover = models.BinaryField(blank=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     location = models.CharField(max_length=100)
#     time = models.DateTimeField()
#     owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     type = models.CharField(
#         max_length=100,
#         choices=typeChoices,

#     )
