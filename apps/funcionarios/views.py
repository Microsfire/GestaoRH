from django.views.generic import ListView
from .models import Funcionario

class FuncionarioList(ListView):
    model = Funcionario





