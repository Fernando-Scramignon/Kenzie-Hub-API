from rest_framework.serializers import ModelSerializer

from .models import Work

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        exclude = ['user']


        exclude = ['user']
        read_only_fields = ['id', 'created_at', 'updated_at']