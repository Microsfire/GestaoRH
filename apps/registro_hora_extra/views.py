import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .form import RegistroHraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHraExtraForm
    #success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraDelite(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    model = RegistroHoraExtra
    form_class = RegistroHraExtraForm


#Teste jquery
class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilzada = True
        registro_hora_extra.save()
        empregado = self.request.user.funcionario

        response = json.dumps(
            {
                'mensagem': 'requisicao executada',
                'horas': float(empregado.total_hora_extra)
            }
        )
        return HttpResponse(response, content_type='application/json')

