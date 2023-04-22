from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models.query import QuerySet

from .serializers import UserSerializer
from .models import User

import pdb

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        user_id = self.request.user.id

        if isinstance(queryset, QuerySet):
            queryset = self.queryset.filter(id__exact=user_id)
            
        return queryset

    