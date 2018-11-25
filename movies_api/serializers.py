from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfiles """
    class Meta:
        model=models.UserProfile
        fields=('id', 'email', 'name','password')
        extra_kwargs={'password':{'write_only':True}}#so it won't be read
    
    def create(self,validated_data):

        user=models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movies, use user_profile as foreign key"""
    class Meta:
        model=models.Movie
        fields=('id', 'user_profile', 'title', 'duration','year','director','writer')                
        extra_kwargs={'user_profile':{'read_only':True}}

