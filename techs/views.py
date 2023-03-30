# rest framework
from rest_framework.generics import ListCreateAPIView 

# authentication and authorization
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# app
from .models import Tech
from .serializers import TechSerializer

# debugger
import ipdb

class TechView(ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # saves user from Token (instead of directly from request data)
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        # only allow the current user tech's to be displayed
        return self.queryset.filter(user_id=self.request.user.id)
