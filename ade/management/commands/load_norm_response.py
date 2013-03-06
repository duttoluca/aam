import glob
import datetime
import os.path
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings
from ade.models import ADE_request, ADE_detail
from django.utils.encoding import smart_unicode
from django.db import transaction


# inserire controlli
class Command(BaseCommand):
    help = "Acquisisce ritorno dal normalizzatore"

    @transaction.commit_on_success()
    def handle(self, *args, **options):
        # per ogni file di tipo ADE_in una cartella
        files = glob.glob(os.path.join(settings.ADE_INPUT_DIR,
                                       "NORM_OUT_ADE_AAM_*"))
        for f in files:
            filename = os.path.basename(f).partition('.')[0]
            pk = int(filename.split('_')[4])
            try:
                req = ADE_request.objects.get(id=pk, status__gt=0)
                for l in file(f, "rb"):
                    line = smart_unicode(l, encoding='latin_1')  # unicode
                    cfisc_orig = line[28:44]
                    comune_residenza_norm = line[757:807]
                    prov_residenza_norm = line[862:864]
                    CAP_residenza_norm = line[857:862]
                    sedime_residenza_norm = line[944:969]
                    nome_via_residenza_norm = line[969:1019]
                    civico_residenza_norm = line[1019:1024]
                    esponente_norm = line[1024:1099]
                    cod_err1_norm = line[749:753]
                    cod_err2_norm = line[753:757]
                    indirizzo_breve_norm = line[1132:1182]
                    #update
                    ADE_detail.objects.filter(ADE_request=pk, cfisc_orig=cfisc_orig).update(comune_residenza_norm=comune_residenza_norm,
                                                                                            prov_residenza_norm=prov_residenza_norm,
                                                                                            CAP_residenza_norm=CAP_residenza_norm,
                                                                                            sedime_residenza_norm=sedime_residenza_norm,
                                                                                            nome_via_residenza_norm=nome_via_residenza_norm,
                                                                                            civico_residenza_norm=civico_residenza_norm,
                                                                                            esponente_norm=esponente_norm,
                                                                                            cod_err1_norm=cod_err1_norm,
                                                                                            cod_err2_norm=cod_err2_norm,
                                                                                            indirizzo_breve_norm=indirizzo_breve_norm
                                                                                            )
                req.status = 3
                req.return_date_norm = datetime.datetime.now()
                req.save()
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))
            except (ADE_request.DoesNotExist, ADE_detail.DoesNotExist, ADE_request.MultipleObjectsReturned):
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))

