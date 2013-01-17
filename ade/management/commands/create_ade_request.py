from django.core.management.base import BaseCommand
from ade.models import ADE_request, ADE_detail


class Command(BaseCommand):
    help = "Crea le richieste AdE"

    def handle(self, *args, **options):
        self.stdout.write( "Hello" )
