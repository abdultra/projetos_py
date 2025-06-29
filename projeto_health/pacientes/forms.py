from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Paciente

class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			'nome', 'nascimento', 'genero', 'telefone',
			'nacionalidade', 'residencia', 'enfermaria',
			'tipo_sanguineo', 'identificacao'
		]
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
			'nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
			'genero': forms.Select(attrs={'class': 'form-control'}),
			'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: +258841234567'}),
			'nacionalidade': forms.Select(attrs={'class': 'form-control'}),
			'residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Pemba'}),
			'enfermaria': forms.Select(attrs={'class': 'form-control'}),
			'tipo_sanguineo': forms.Select(attrs={'class': 'form-control'}),
			'identificacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BI ou NUIT'}),
		}

	def clean_nascimento(self):
		nascimento = self.cleaned_data.get('nascimento')
		if nascimento and nascimento > date.today():
			raise ValidationError("A data de nascimento não pode ser no futuro.")
		return nascimento
