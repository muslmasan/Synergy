# from django.db import models
# from home.models import UserProfile

# # Create your models here.
# typeChoices = (
#     ("PUBLIC","Public"),
#     ("PRIVATE","Private"),
# )
# categoriesChoices = (
#     ("PROGRAMMING","Programming"),
#     ("DESIGN","Design")
# )

# class Community (models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     icon = models.BinaryField(blank=True)
#     cover = models.BinaryField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
#     particpatance = models.ManyToManyField(UserProfile, related_name='participatance')
#     type = models.CharField(
#         max_length=100,
#         choices=typeChoices
#     )
#     category = models.CharField(
#         max_length=100,
#         choices=categoriesChoices,
#     )

#     def __str__(self):
#         return self.title


# class Post(models.Model):
#     body = models.TextField(blank=True)
#     image = models.BinaryField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     Community = models.ForeignKey(Community, on_delete=models.CASCADE)
#     owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.body.strip()}'

# class Comment(models.Model):
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     Post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.pk}'
