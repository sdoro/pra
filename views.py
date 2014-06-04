
from django.http import HttpResponse
from pra.models import *

# q1:  La lista delle automobili immatricolate in un certo anno
def q1(request):
    elenco = "Lista delle automobili immatricolate nel 2013<br>"
    vs = veicolo.objects.all()
    vs = vs.filter(data_im__range=["2013-01-01", "2013-12-31"])
    for v in vs:
        elenco += "%s<br>" % (v.targa)
    return HttpResponse(elenco)

# q2: Per ogni modello, il numero di veicoli immatricolati tra il 2010 e il
#     2014, solo se superiore a uno.
from django.db.models import Count
def q2(request):
    elenco = ""
    vs = veicolo.objects.all()
    vs = vs.filter(data_im__range=["2010-01-01", "2013-12-31"])
    vs = vs.filter(data_omo__isnull=False)   # non vogliamo i prototipi
    vs = vs.values('nome').annotate(cnt=Count('nome'))
    for v in vs:
        if v['cnt'] > 1:
           elenco += "%s - %s<br>" % (v['nome'], v['cnt'])
    if elenco == "":
        elenco = "Nessun risultato"
    return HttpResponse(elenco)

# q3. L'elenco delle patenti in scadenza in ordine di prefettura
import datetime
def q3(request):
    elenco = ""
    ps = patente.objects.all()
    ps = ps.filter(data_scadenza__lt=datetime.date(2014, 6, 23))
    ps = ps.order_by('prefettura')
    for p in ps:
        elenco += "%s - %s<br>" % (p.cod_pat, p.prefettura)
    return HttpResponse(elenco)

# q4: Numero massimo di patentati ultrasessantenni nelle province di Venezia,
#     Treviso, Padova
from django.db import connection
def q4(request):
    elenco = "Numero max: "
    query = '''
SELECT max(totale)
FROM
  (SELECT i.prov,
          count(i.prov) AS totale
   FROM pra_intestatario AS i
   INNER JOIN pra_patente AS p ON p.idI_id = i.idI
   WHERE i.prov IN ('VE',
                    'TV',
                    'PD')
     AND i.data_nascita < '1954-05-23'
   GROUP BY i.prov) AS over60'''

    cursor = connection.cursor()
    cursor.execute(query)
    elenco += "%s<br>" % cursor.fetchall()[0]

    return HttpResponse(elenco)

