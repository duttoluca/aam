from django.db import models

from django.db.models import permalink


class ADE_request(models.Model):

    STATUS_CHOICES = (
    (0, 'Inserito'),
    (1, 'Richiesto'),
    (2, 'Ritornato'),
    (99, 'Eliminato'),
)

    original_filename = models.CharField(max_length=255,
                                         help_text="Nome del file originale",
                                         verbose_name="Richiesta")
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 verbose_name="Status",
                                 help_text="Stato della richiesta")
    insert_date = models.DateTimeField(verbose_name="Data inserimento",
                                       help_text="Data inserimento richiesta")
    return_date = models.DateTimeField(verbose_name="Data ritorno",
                                       help_text="Data ritorno richiesta",
                                       blank=True,
                                       null=True)

    def __unicode__(self):
        return self.original_filename

    class Meta:
        ordering = ['insert_date']
        verbose_name = 'Richiesta AdE'
        verbose_name_plural = 'Richieste AdE'


class ADE_detail(models.Model):
    cfisc_orig = models.CharField(max_length=16,
                             help_text="Codice Fiscale Originale",
                             verbose_name="Codice Fiscale Originale")
    cfisc = models.CharField(max_length=16,
                             help_text="Codice Fiscale",
                             verbose_name="Codice Fiscale",
                             blank=True)
    sogg_valido = models.CharField(max_length=1, blank=True),
    cc1 = models.CharField(max_length=1, blank=True),
    cc2 = models.CharField(max_length=1, blank=True),
    cognome_denominazione = models.CharField(max_length=150,
                                             verbose_name="Cognome/Denominazione",
                                             help_text="Cognome/Denominazione",
                                             blank=True)
    nome_acronimo = models.CharField(max_length=40,
                                             verbose_name="Nome/Acronimo",
                                             help_text="Nome/Acronimo",
                                             blank=True)
    sesso = models.CharField(max_length=1, blank=True)
    data_nascita = models.CharField(max_length=8, blank=True)
    cod_belfiore_nascita = models.CharField(max_length=4, blank=True)
    comune_nascita = models.CharField(max_length=45, blank=True)
    prov_nascita = models.CharField(max_length=2, blank=True)
    cod_belfiore_residenza = models.CharField(max_length=4, blank=True)
    comune_residenza = models.CharField(max_length=45, blank=True)
    prov_residenza = models.CharField(max_length=2, blank=True)
    CAP_residenza = models.CharField(max_length=5, blank=True)
    fonte = models.CharField(max_length=1, blank=True)
    data_fonte = models.CharField(max_length=8, blank=True)
    sedime_residenza = models.CharField(max_length=25, blank=True)
    nome_via_residenza = models.CharField(max_length=70, blank=True)
    civico_residenza = models.CharField(max_length=60, blank=True)
    ind_norm = models.CharField(max_length=1, blank=True)
    ind_decesso = models.CharField(max_length=1, blank=True)
    data_decesso = models.CharField(max_length=8, blank=True)
    ind_conf_comune = models.CharField(max_length=1, blank=True)
    nat_giurid = models.CharField(max_length=1, blank=True)
    ADE_request = models.ForeignKey(ADE_request)

    def __unicode__(self):
        return self.cfisc_orig

    class Meta:
        ordering = ['ADE_request', 'cfisc_orig']
        verbose_name = 'Dettaglio AdE'
        verbose_name_plural = 'Dettagli AdE'
