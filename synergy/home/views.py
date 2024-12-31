from django.shortcuts import render
from .serializers import UserSerializer
from .models import UserProfile
from rest_framework import viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserView(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

#     queryset = UserProfile.objects.all( )
#     serializer_class = UserSerializer
# class UserView(viewsets.ModelViewSet):


