from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.conf import settings

from ade.models import ADE_request


# TODO spostare i file dopo fatti
# inserire controlli
class Command(BaseCommand):
    EXPIRE_DAYS = 30
    help = 'Elimina le richieste AdE oltre i ' + str(settings.REQUEST_EXPIRATION_DAYS) +' giorni'

    def handle(self, *args, **options):
        expiration_date = datetime.now() - timedelta(settings.REQUEST_EXPIRATION_DAYS)
        #eliminazione delle richieste
        #ON DELETE CASCADE implicito per eliminare i dettagli
        ADE_request.objects.filter(status__gt=0,
                                   insert_date__lte=expiration_date)
