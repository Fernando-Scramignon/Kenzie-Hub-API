from rest_framework.serializers import ModelSerializer
from .models import Tech


class TechSerializer(ModelSerializer):

    class Meta:
        model = Tech

        exclude = ['user']
        read_only_fields = ['id', 'created_at', 'updated_at']