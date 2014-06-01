
from django.db import models


class utente_web (models.Model):
	CF = models.CharField(primary_key=True, max_length=16)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s %s' % (self.CF, self.username)

	class Meta:
		verbose_name_plural = "Utenti"


class tipologia (models.Model):
	id_tipo = models.IntegerField(primary_key=True)
	descrizione = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.id_tipo, self.descrizione)

	class Meta:
		verbose_name_plural = "Tipologie"

class intestatario (models.Model):
	idI = models.IntegerField(primary_key=True)
	CF = models.CharField(max_length=16)
	PI = models.CharField(max_length=20)
	data_nascita = models.DateField()
	indirizzo = models.CharField(max_length=40)
	cognome = models.CharField(max_length=30)
	nome = models.CharField(max_length=30)
	prov = models.CharField(max_length=4)

	def __unicode__(self):
		return u'%s (CF:%s, PI:) %s %s %s %s' % (self.idI, self.CF, self.PI, self.data_nascita, self.indirizzo, self.cognome, self.nome)

	class Meta:
		verbose_name_plural = "Intestatari"

class veicolo (models.Model):
	targa = models.CharField(primary_key=True, max_length=10)
	ntelaio = models.IntegerField()
	nome = models.CharField(max_length=15)
	data_im = models.DateField()
	data_omo = models.DateField(null=True)
	id_tipo = models.ForeignKey('tipologia')
	idI = models.ForeignKey('intestatario')

	def __unicode__(self):
		return u'%s %s (im:%s, om:) %s %s' % (self.targa, self.ntelaio, self.data_im, self.data_omo, self.id_tipo, self.idI)

	class Meta:
		verbose_name_plural = "Veicoli"


class patente (models.Model):
	cod_pat = models.CharField(primary_key=True, max_length=15)
	data_rilascio = models.DateField()
	data_scadenza = models.DateField()
	idI = models.ForeignKey('intestatario')
	prefettura = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s (%s, %s) %s %s' % (self.cod_pat, self.data_rilascio, self.data_scadenza, self.idI, self.prefettura)

	class Meta:
		verbose_name_plural = "Patenti"


class accesso_patente (models.Model):
	CF = models.ForeignKey('utente_web')
	cod_pat = models.ForeignKey('patente')
	data = models.DateField()

	def __unicode__(self):
		return u'%s %s %s' % (self.CF, self.cod_pat, self.data)

	class Meta:
		verbose_name_plural = "Accessi Patente"


class accesso_veicolo (models.Model):
	CF = models.ForeignKey('utente_web')
	targa = models.ForeignKey('veicolo')
	data = models.DateField()

	def __unicode__(self):
		return u'%s %s %s' % (self.targa, self.CF, self.data)

	class Meta:
		verbose_name_plural = "Accessi Veicolo"


