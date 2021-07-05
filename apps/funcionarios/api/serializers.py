from apps.funcionarios.models import Funcionario
from rest_framework import serializers
from apps.registro_hora_extra.api.serializers import RegistoHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistoHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ['user', 'nome', 'departamentos', 'empresa', 'imagem',
                  'registrohoraextra_set', 'total_hora_extra']
