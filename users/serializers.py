from rest_framework import serializers

from .models import User
from techs.serializers import TechSerializer

class UserSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True, required=False)

    class Meta:
        model = User

        fields = [
            'id', 'name', 'email','password',
            'course_module','bio','contact',
            'created_at', 'updated_at','avatar_url', 'techs'
        ]
        

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)