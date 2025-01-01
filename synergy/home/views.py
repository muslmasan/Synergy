from django.shortcuts import render
from .serializers import UserSerializer,UserCreateSerializer
from .models import UserProfile
from rest_framework import viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class UserView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class GetUser(generics.RetrieveAPIView):

    queryset= UserProfile.objects.all()
    serializer_class= UserSerializer
    permission_classes =[AllowAny]
    lookup_field = 'id'

