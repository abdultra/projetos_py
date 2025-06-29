from django.db import models
from django_countries.fields import CountryField
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

from datetime import date

class Enfermaria(models.Model):
	class Proveniencia(models.TextChoices):
		SUR = 'SUR', 'Serviço de Urgência e Reanimação'
		PED = 'PED', 'Pediatria'
		CIR = 'CIR', 'Cirurgia'
		GIN = 'GIN', 'Ginecologia'
		OBST = 'OBST', 'Obstetrícia'
		UROL = 'UROL', 'Urologia'
		MED_I = 'MED_I', 'Medicina - Homens'
		MED_II = 'MED_II', 'Medicina - Mulheres'
		OFT = 'OFT', 'Oftalmologia'
		C_EXT = 'C.EXT', 'Consulta Externa'

	enfermaria = models.CharField(max_length=225, choices=Proveniencia.choices)

	def __str__(self):
		return self.get_enfermaria_display()

class TipoSanguineo(models.Model):
	TIPO_CHOICES = [
		('A+', 'A+'), ('A-', 'A-'),
		('B+', 'B+'), ('B-', 'B-'),
		('AB+', 'AB+'), ('AB-', 'AB-'),
		('O+', 'O+'), ('O-', 'O-'),
	]

	tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, unique=True)

	class Meta:
		verbose_name = "Tipo Sanguíneo"
		verbose_name_plural = "Tipos Sanguíneos"

	def __str__(self):
		return self.tipo

class Paciente(models.Model):
	nome = models.CharField(max_length=255)
	nascimento = models.DateField()
	genero = models.CharField(
		max_length=10,
		choices=[
			("Masculino", "Masculino"),
			("Feminino", "Feminino"),
			("Outro", "Outro"),
		],
	)
	enfermaria = models.ForeignKey(Enfermaria, on_delete=models.CASCADE)
	tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.CASCADE)
	telefone = PhoneNumberField(region="MZ", max_length=13)
	residencia = models.CharField(max_length=100, blank=True, null=True)
	nacionalidade = CountryField(blank=False, null=False, default="MZ")
	identificacao = models.CharField(max_length=20, blank=True, null=True)
	entrada = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Pacientes"

	def __str__(self):
		return self.nome

	@property
	def idade(self):
		hoje = date.today()
		return hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))

	def clean(self):
		if self.nascimento > date.today():
			raise ValidationError("A data de nascimento não pode ser no futuro.")