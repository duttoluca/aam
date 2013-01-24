aam
===

AdE Automated Manager
Automatizza la gestione di richieste AdE (Agenzia delle Entrate).

Tramite batch schedulabili crea le richieste e acquisisce i ritorni.

Tramite interfaccia web permette di monitorare la richiesta e scaricare l'excel.

Funzionamento:

Inserire i file di richiesta (contenenti l'elenco dei CF) nella cartella input con formato ADE_REQ_yyyymmdd_xxxx.TXT

Il batch load_cfisc consuma questi file e crea le richieste.

Il batch create_ade_request crea i file da inviare a AdE nella cartella output (ADE_AAM_[PF|PG]_yyyymmdd_pk.TXT).

Il batch load_ade_response recupera i file ESITO_ADE_AAM_[PF|PG]_* e carica gli esiti relativi sul db.

Da interfaccia web si possono consultare le richieste e relativo stato, gli esiti eventualmente ricevuti, e scaricare reportistica.
