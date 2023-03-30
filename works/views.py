
# authentication and authorization
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# rest framework
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_409_CONFLICT

# app
from .models import Work
from .serializers import WorkSerializer

# Create your views here.
class WorkView(ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        works = self.request.user.works.all()
        title = self.request.data['title']

        is_title_unique = True

        for work in works:
            if work.title == title:
                is_title_unique = False

        if not is_title_unique:
            raise ValidationError({'title': 'You alread registered this work'}, HTTP_409_CONFLICT)

        # saves user from Token (instead of directly from request data)
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # only allow the current user tech's to be displayed
        return self.queryset.filter(user_id=self.request.user.id)
    