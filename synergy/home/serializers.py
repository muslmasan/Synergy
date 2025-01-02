from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id','username','first_name','last_name','email','cover', 'image','gender']


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username','password','first_name','last_name','email','cover', 'image','gender']