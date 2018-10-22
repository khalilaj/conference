from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Conference
from ..core.auth import JwtAuth
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .renderer import BusinessRenderer


class ConferenceListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (BusinessRenderer,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Conference.objects.all()


class ConferenceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Conference.objects.all()
