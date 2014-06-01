
from django.http import HttpResponse
from pra.models import *

def q1(request):
    elenco = ""
    for v in veicolo.objects.all():
        elenco += "%s<br>" % (v.targa)
    return HttpResponse(elenco)

def q2(request):
    elenco = ""
    vs = veicolo.objects.all()
    vs = vs.filter(data_im__range=["2013-01-01", "2013-12-31"])
    vs = vs.filter(data_omo__isnull=False)   # non vogliamo i prototipi
    for v in vs:
        elenco += "%s<br>" % (v.targa)
    return HttpResponse(elenco)

import datetime
def q3(request):
    elenco = ""
    ps = patente.objects.all()
    ps = ps.filter(data_scadenza__lt=datetime.date(2014, 6, 23))
    for p in ps:
        elenco += "%s<br>" % (p.cod_pat)
    return HttpResponse(elenco)

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
    #elenco += "%s<br>" % cursor.fetchall()

    return HttpResponse(elenco)

