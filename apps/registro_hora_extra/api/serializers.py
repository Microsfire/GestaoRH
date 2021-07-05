from apps.registro_hora_extra.models import RegistroHoraExtra
from rest_framework import serializers


class RegistoHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['funcionario', 'motivo', 'horas', 'utilzada']
