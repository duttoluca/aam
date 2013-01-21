from django.views.generic import ListView  # DetailView

from models import ADE_request


class ADE_requestListView(ListView):
    def get_queryset(self):
        return ADE_request.objects.all()
