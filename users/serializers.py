from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'id', 'name', 'email',
            'course_module','bio','contact',
            'created_at', 'updated_at','avatar_url',
        ]
        

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)