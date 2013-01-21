from django.views.generic import ListView, DetailView

from models import ADE_request


class ADE_requestListView(ListView):
    model = ADE_request


class ADE_requestDetailView(DetailView):
    model = ADE_request
