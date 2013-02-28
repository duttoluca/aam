import glob
import datetime
import os.path
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings
from ade.models import ADE_request, ADE_detail


# inserire controlli
class Command(BaseCommand):
    help = "Acquisisce risposta AdE"

    def handle(self, *args, **options):
        # per ogni file di tipo ADE_in una cartella
        files = glob.glob(os.path.join(settings.ADE_INPUT_DIR,
                                       "ESITO_ADE_AAM_*"))
        for f in files:
            filename = os.path.basename(f).partition('.')[0]
            pk = int(filename.split('_')[5])
            try:
                req = ADE_request.objects.get(id=pk, status__gt=0)
                for l in file(f, "rb"):
                    line = unicode(l, errors='strict')  # convert to unicode
                    if (line[0] == '1' or line[0] == '2'):
                        if line[0] == '1':
                            p_fisica = True
                        else:
                            p_fisica = False
                        cfisc_orig = line[16:32].strip()
                        #print cfisc_orig
                        details = ADE_detail.objects.filter(ADE_request=pk, cfisc_orig=cfisc_orig)
                        for detail in details:
                            detail.cfisc = line[228:244].strip()
                            detail.sogg_valido = line[244:245].strip()
                            detail.cc1 = line[245:246].strip()
                            detail.cc2 = line[246:247].strip()
                            if p_fisica:
                                detail.cognome_denominazione = line[247:287].strip()
                                detail.nome_acronimo = line[287:327].strip()
                                detail.sesso = line[327:328].strip()
                                detail.data_nascita = line[328:336].strip()
                                detail.cod_belfiore_nascita = line[336:340].strip()
                                detail.comune_nascita = line[340:385].strip()
                                detail.prov_nascita = line[385:387].strip()
                                detail.cod_belfiore_residenza = line[387:391].strip()
                                detail.comune_residenza = line[391:436].strip()
                                detail.prov_residenza = line[436:438].strip()
                                detail.CAP_residenza = line[438:443].strip()
                                detail.fonte = line[443:444].strip()
                                detail.data_fonte = line[444:452].strip()
                                detail.sedime_residenza = line[452:477].strip()
                                detail.nome_via_residenza = line[477:547].strip()
                                detail.civico_residenza = line[547:607].strip()
                                detail.ind_norm = line[607:608].strip()
                                detail.ind_decesso = line[608:609].strip()
                                detail.data_decesso = line[609:617].strip()
                                detail.ind_conf_comune = line[617:618].strip()
                            else:
                                detail.cognome_denominazione = line[247:397].strip()
                                detail.nome_acronimo = line[397:412].strip()
                                detail.cod_belfiore_residenza = line[414:418].strip()
                                detail.comune_residenza = line[418:463].strip()
                                detail.prov_residenza = line[463:465].strip()
                                detail.CAP_residenza = line[465:470].strip()
                                detail.fonte = line[470:471].strip()
                                detail.data_fonte = line[471:479].strip()
                                detail.sedime_residenza = line[479:504].strip()
                                detail.nome_via_residenza = line[504:574].strip()
                                detail.civico_residenza = line[574:599].strip()
                                detail.ind_norm = line[634:635].strip()
                            try:
                                detail.save()
                            except Exception:
                                print line
                req.status = 2
                req.return_date = datetime.datetime.now()
                req.save()
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))
            except (ADE_request.DoesNotExist, ADE_detail.DoesNotExist, ADE_request.MultipleObjectsReturned):
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))

