from django.shortcuts import render
from .serializers import UserSerializer,UserCreateSerializer
from .models import UserProfile
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        return True


class GetUser(generics.RetrieveAPIView):

    queryset= UserProfile.objects.all()
    serializer_class= UserSerializer
    permission_classes =[AllowAny]
    lookup_field = 'id'

