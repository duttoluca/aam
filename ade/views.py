from datetime import datetime, date
from django.http import HttpResponse
import xlwt

from django.views.generic import ListView, DetailView

from models import ADE_request, ADE_detail


class ADE_requestListView(ListView):
    model = ADE_request


class ADE_requestDetailView(DetailView):
    model = ADE_request

    def get_context_data(self, **kwargs):
        context = super(ADE_requestDetailView, self).get_context_data(**kwargs)
        req = self.get_object()
        context['details'] = ADE_detail.objects.filter(ADE_request=req.pk)[:1000]
        return context


def create_xls(request, pk):
    book = xlwt.Workbook(encoding='utf8')
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')

    req = ADE_request.objects.get(id=pk)
    details = ADE_detail.objects.filter(ADE_request=pk)

    sheet = book.add_sheet('Richiesta ADE')

    sheet.write(0, 0, 'Dettaglio richiesta AdE', style=default_style)
    sheet.write(2, 0, 'File originale', style=default_style)
    sheet.write(3, 0, 'Data inserimento', style=default_style)
    sheet.write(4, 0, 'Data ritorno', style=default_style)
    sheet.write(5, 0, 'Stato richiesta', style=default_style)

    sheet.write(2, 1, req.original_filename, style=default_style)
    sheet.write(3, 1, req.insert_date, style=datetime_style)
    sheet.write(4, 1, req.return_date, style=datetime_style)
    sheet.write(5, 1, req.get_status_display(), style=default_style)

    sheet.write(7, 0, 'CFISC ORIGINALE', style=default_style)
    sheet.write(7, 1, 'CFISC', style=default_style)
    sheet.write(7, 2, 'COGN/DEN', style=default_style)
    sheet.write(7, 3, 'NOME/ACRONIMO', style=default_style)
    sheet.write(7, 4, 'SESSO', style=default_style)
    sheet.write(7, 5, 'COMUNE RES.', style=default_style)
    sheet.write(7, 6, 'PROV. RES.', style=default_style)
    sheet.write(7, 7, 'CAP RES.', style=default_style)
    sheet.write(7, 8, 'SEDIME RES.', style=default_style)
    sheet.write(7, 9, 'VIA RES.', style=default_style)
    sheet.write(7, 10, 'CIVICO RES.', style=default_style)
    sheet.write(7, 11, 'DATA DECESSO', style=default_style)
    sheet.write(7, 12, 'DATA FONTE', style=default_style)

    for row, detail in enumerate(details, start=8):
        sheet.write(row, 0, detail.cfisc_orig, style=default_style)
        sheet.write(row, 1, detail.cfisc, style=default_style)
        sheet.write(row, 2, detail.cognome_denominazione, style=default_style)
        sheet.write(row, 3, detail.nome_acronimo, style=default_style)
        sheet.write(row, 4, detail.sesso, style=default_style)
        sheet.write(row, 5, detail.comune_residenza, style=default_style)
        sheet.write(row, 6, detail.prov_residenza, style=default_style)
        sheet.write(row, 7, detail.CAP_residenza, style=default_style)
        sheet.write(row, 8, detail.sedime_residenza, style=default_style)
        sheet.write(row, 9, detail.nome_via_residenza, style=default_style)
        sheet.write(row, 10, detail.civico_residenza, style=default_style)
        sheet.write(row, 11, detail.data_decesso, style=default_style)
        sheet.write(row, 12, detail.data_fonte, style=default_style)

    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=richiesta_' + str(req.pk).rjust(5, '0') + '.xls'
    book.save(response)
    return response
