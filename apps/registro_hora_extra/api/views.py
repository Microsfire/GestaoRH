from apps.registro_hora_extra.models import RegistroHoraExtra
from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import RegistoHoraExtraSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):

    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistoHoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
