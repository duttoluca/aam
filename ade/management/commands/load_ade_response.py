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
    help = "Acquisisce risposta AdE"
    
    @transaction.commit_on_success()
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
                    line = smart_unicode(l, encoding='latin_1')  # unicode
                    if (line[0] == '1' or line[0] == '2'):
                        if line[0] == '1':
                            p_fisica = True
                        else:
                            p_fisica = False
                        cfisc_orig = line[16:32].strip()
                        #print cfisc_orig
                        #update
                        cfisc = line[228:244].strip()
                        sogg_valido = line[244:245].strip()
                        cc1 = line[245:246].strip()
                        cc2 = line[246:247].strip()
                        if p_fisica:
                            cognome_denominazione = line[247:287].strip()
                            nome_acronimo = line[287:327].strip()
                            sesso = line[327:328].strip()
                            data_nascita = line[328:336].strip()
                            cod_belfiore_nascita = line[336:340].strip()
                            comune_nascita = line[340:385].strip()
                            prov_nascita = line[385:387].strip()
                            cod_belfiore_residenza = line[387:391].strip()
                            comune_residenza = line[391:436].strip()
                            prov_residenza = line[436:438].strip()
                            CAP_residenza = line[438:443].strip()
                            fonte = line[443:444].strip()
                            data_fonte = line[444:452].strip()
                            sedime_residenza = line[452:477].strip()
                            nome_via_residenza = line[477:547].strip()
                            civico_residenza = line[547:607].strip()
                            ind_norm = line[607:608].strip()
                            ind_decesso = line[608:609].strip()
                            data_decesso = line[609:617].strip()
                            ind_conf_comune = line[617:618].strip()
                        else:
                            cognome_denominazione = line[247:397].strip()
                            nome_acronimo = line[397:412].strip()
                            cod_belfiore_residenza = line[414:418].strip()
                            comune_residenza = line[418:463].strip()
                            prov_residenza = line[463:465].strip()
                            CAP_residenza = line[465:470].strip()
                            fonte = line[470:471].strip()
                            data_fonte = line[471:479].strip()
                            sedime_residenza = line[479:504].strip()
                            nome_via_residenza = line[504:574].strip()
                            civico_residenza = line[574:599].strip()
                            ind_norm = line[634:635].strip()
                        #update
                        details = ADE_detail.objects.filter(ADE_request=pk, cfisc_orig=cfisc_orig)
                        #print details
                        details.update(cfisc=cfisc,
                                                                                                sogg_valido=sogg_valido,
                                                                                                cc1=cc1,
                                                                                                cc2=cc2,
                                                                                                cognome_denominazione=cognome_denominazione,
                                                                                                nome_acronimo=nome_acronimo,
                                                                                                sesso=sesso,
                                                                                                data_nascita=data_nascita,
                                                                                                cod_belfiore_nascita=cod_belfiore_nascita,
                                                                                                comune_nascita=comune_nascita,
                                                                                                prov_nascita=prov_nascita,
                                                                                                cod_belfiore_residenza=cod_belfiore_residenza,
                                                                                                comune_residenza=comune_residenza,
                                                                                                prov_residenza=prov_residenza,
                                                                                                CAP_residenza=CAP_residenza,
                                                                                                fonte=fonte,
                                                                                                data_fonte=data_fonte,
                                                                                                sedime_residenza=sedime_residenza,
                                                                                                nome_via_residenza=nome_via_residenza,
                                                                                                civico_residenza=civico_residenza,
                                                                                                ind_norm=ind_norm,
                                                                                                ind_decesso=ind_decesso,
                                                                                                data_decesso=data_decesso,
                                                                                                ind_conf_comune=ind_conf_comune
                                                                                                )
                req.status = 2
                req.return_date = datetime.datetime.now()
                req.save()
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))
            except (ADE_request.DoesNotExist, ADE_detail.DoesNotExist, ADE_request.MultipleObjectsReturned):
                shutil.move(f, os.path.join(settings.ADE_ARCHIVE_DIR, 'INPUT'))

