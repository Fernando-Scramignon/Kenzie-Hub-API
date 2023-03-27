from rest_framework.serializers import ModelSerializer
from .models import Tech
from users.serializers import UserSerializer

class TechSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tech

        field = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']