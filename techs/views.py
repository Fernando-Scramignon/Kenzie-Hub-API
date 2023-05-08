# rest framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_409_CONFLICT

# authentication and authorization
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner

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

    # It doesn't need to be unique, only unique amoung the user's techs

    def perform_create(self, serializer):

        techs = self.request.user.techs.all()
        title = self.request.data['title']

        is_title_unique = True

        for tech in techs:
            if tech.title == title:
                is_title_unique = False

        if not is_title_unique:
            raise ValidationError({'title':'you already registered this tech'}, HTTP_409_CONFLICT)

        # saves user from Token (instead of directly from request data)
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        # only allow the current user tech's to be displayed
        return self.queryset.filter(user_id=self.request.user.id)

class TechDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    # It doesn't need to be unique, only unique amoung the user's techs

    def perform_update(self, serializer):

        techs = self.request.user.techs.all()
        title = self.request.data['title']

        is_title_unique = True

        for tech in techs:
            if tech.title == title:
                is_title_unique = False

        if not is_title_unique:
            raise ValidationError({'title':'you already registered this tech'}, HTTP_409_CONFLICT)

        # saves user from Token (instead of directly from request data)
        serializer.save(user=self.request.user)