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
        context['details'] = ADE_detail.objects.filter(ADE_request=req.pk)
        return context


def create_xls(request, pk):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('indirizzi')

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    values_list = ADE_detail.objects.filter(ADE_request=pk).values_list()

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style

            sheet.write(row, col, val, style=style)

    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=example.xls'
    book.save(response)
    return response
