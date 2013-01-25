import glob
import datetime
import os.path
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from ade.models import ADE_request, ADE_detail


# TODO spostare i file dopo fatti
# inserire controlli
class Command(BaseCommand):
    help = "Acquisisce elenco cfisc per richiesta AdE"

    def handle(self, *args, **options):
        # per ogni file di tipo ADE_in una cartella
        files = glob.glob(os.path.join(settings.ADE_INPUT_DIR,
                                       "ADE_REQ_*"))
        for f in files:
        #crea nuova ADE_request
            filename = os.path.basename(f)
            #print filename
            r = ADE_request(original_filename=filename,
                            insert_date=datetime.datetime.now())
            r.save()
            for line in file(f, "rb"):
                if line.strip() != '':
                    d = ADE_detail(cfisc_orig=line[:16].strip().upper(),
                                   ADE_request=r)
                    d.save()
            #sposta file in archivio
            shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))
