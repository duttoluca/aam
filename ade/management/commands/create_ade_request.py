from django.core.management.base import BaseCommand
from ade.models import ADE_request, ADE_detail


class Command(BaseCommand):
    help = "Crea le richieste AdE"

    def handle(self, *args, **options):
        ADE_HEADER = "080087670016     REGIONE PIEMONTE                                            ZNLFRZ59L25H620OZANELLA                                 FABRIZIO                                M25071959ROVIGO                                       RO                                                                      A\n"
        ADE_FOOTER = "980087670016     REGIONE PIEMONTE                                            ZNLFRZ59L25H620OZANELLA                                 FABRIZIO                                M25071959ROVIGO                                       RO          000159000149000008                                          A\n"
        #self.stdout.write( "Hello" )
        r_list = ADE_request.objects.filter(status=0)
        for r in r_list:
            self.stdout.write(ADE_HEADER)
            d_list = ADE_detail.objects.filter(ADE_request__id=r.id)
            for d in d_list:
                self.stdout.write("1____" + d.cfisc_orig+"\n")
            self.stdout.write(ADE_FOOTER)
