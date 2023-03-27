from rest_framework.generics import ListCreateAPIView 

from .models import Tech
from .serializers import TechSerializer

class TechView(ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
