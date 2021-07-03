import csv
import json
import xlwt

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


class ExportarParaCsv(View):
    def get (self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        registro_he = RegistroHoraExtra.objects.filter(utilzada=False)
        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas'])

        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.funcionario,
                             registro.funcionario.total_hora_extra, registro.horas])
        return response

class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Relatorio.xls"'

        wb = xlwt.Workbook(encoding='UTF-8')
        ws = wb.add_sheet('banco de horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilzada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_hora_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response


