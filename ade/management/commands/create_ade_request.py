import os.path
from django.core.management.base import BaseCommand
from ade.models import ADE_request, ADE_detail
import aam.settings as settings


class Command(BaseCommand):
    help = "Crea i file di richiesta AdE"

    def handle(self, *args, **options):
        ADE_HEADER = "080087670016     REGIONE PIEMONTE                                            ZNLFRZ59L25H620OZANELLA                                 FABRIZIO                                M25071959ROVIGO                                       RO                                                                      A\n"
        ADE_FOOTER = "980087670016     REGIONE PIEMONTE                                            ZNLFRZ59L25H620OZANELLA                                 FABRIZIO                                M25071959ROVIGO                                       RO          000159000149000008                                          A\n"
        r_list = ADE_request.objects.filter(status=0)
        for r in r_list:
            year = str(r.insert_date.year)
            month = str(r.insert_date.month).rjust(2, '0')
            day = str(r.insert_date.day).rjust(2, '0')
            timestamp = year + month + day
            #self.stdout.write(timestamp)
            # crea file fisiche e giuridiche
            outputFilePF = file(os.path.join(settings.ADE_OUTPUT_DIR,"ADE_AAM_PF_" + timestamp + "_" + str(r.id) + ".TXT"),"wb")
            outputFilePG = file(os.path.join(settings.ADE_OUTPUT_DIR,"ADE_AAM_PG_" + timestamp + "_" + str(r.id) + ".TXT"),"wb")
            outputFilePF.write(ADE_HEADER)
            outputFilePG.write(ADE_HEADER)
            #trova i dettagli associati alla richiesta
            d_list = ADE_detail.objects.select_for_update().filter(ADE_request__id=r.id)
            for d in d_list:
                if len(d.cfisc_orig) == 16:
                    row = "1" + 15 * " " + d.cfisc_orig + 218 * " " + "\n"
                    outputFilePF.write(row)
                elif len(d.cfisc_orig) == 11:
                    row = "2" + 15 * " " + d.cfisc_orig + 218 * " " + "\n"
                    outputFilePG.write(row)
                else:
                    #CFISC errato, non faccio nulla
                    pass
            outputFilePF.write(ADE_FOOTER)
            outputFilePG.write(ADE_FOOTER)
            outputFilePF.close()
            outputFilePG.close()
            # cambia lo status della richiesta
            r.status = 1
            r.save()
