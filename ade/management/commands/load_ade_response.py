import glob
import datetime
import os.path
import shutil
from django.core.management.base import BaseCommand
from ade.models import ADE_request, ADE_detail
import aam.settings as settings


# TODO spostare i file dopo fatti
# inserire controlli
class Command(BaseCommand):
    help = "Acquisisce risposta AdE"


    def handle(self, *args, **options):
        pass
    
    # per ogni file di tipo ESITO_ADE_AAM_[PF|PG]_*
        #estrae la PK
        #se esiste
            #per ogni riga buona del File
            #se esiste il detail corretto
                #popola il detail con i dati mancanti
                #salva il detail
        #Aggiorna data di ritorno e status della richiesta e salva
        #sposta il file in archivio
        