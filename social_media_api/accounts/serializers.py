from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
      followers_count = serializers.SerializerMethodField(read_only=True)
      following_count = serializers.SerializerMethodField(read_only=True)


class Meta:
      model = User
      fields = [
          'id', 'username', 'email', 'first_name', 'last_name',
          'bio', 'profile_picture', 'followers_count', 'following_count',
   ]
      read_only_fields = ['id', 'followers_count', 'following_count']


def get_followers_count(self, obj):
      return obj.followers.count()


def get_following_count(self, obj):
      return obj.following.count()


class RegistrationSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True, min_length=8)

class Meta:
      model = User
      fields = ['username', 'email', 'password']


def create(self, validated_data):
      user = User(
      username=validated_data['username'],
      email=validated_data.get('email', ''),
    )
      user.set_password(validated_data['password'])
      user.save()
      return user