
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello world")

from pra.models import *

def q1(request):
    elenco = ""
    for a in agenzia.objects.all().order_by('nomeAG'):
        elenco += "'%s' in %s, telefono: %s<br>" % (a.nomeAG,
            a.citta, a.telefono)
    return HttpResponse(elenco)



