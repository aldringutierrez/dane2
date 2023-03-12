from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('pais','nacionalidad','sexo','edad','acompanantes','numacompanantes','motivos','organizacion','servicios')

	sexo = forms.ChoiceField(
	choices=Book.Sexo.choices,
	widget=forms.RadioSelect(attrs={
		'hx-trigger': 'change'
	})
    )
	acompanantes = forms.ChoiceField(
	label='Acompañantes',
	choices=Book.Acompanantes.choices,
	widget=forms.RadioSelect(attrs={
		'hx-trigger': 'change'
	})
    )
	motivos = forms.ChoiceField(
	choices=Book.Motivos.choices,
	widget=forms.RadioSelect(attrs={
		'hx-trigger': 'change'
	})
    )
	numacompanantes = forms.CharField(label='Numero de Acompañantes', max_length=30)
	organizacion = forms.ChoiceField(
	choices=Book.Organizacion.choices,
	widget=forms.RadioSelect(attrs={
		'hx-trigger': 'change'
	})
    )
	servicios = forms.ChoiceField(
	choices=Book.Servicios.choices,
	widget=forms.RadioSelect(attrs={
		'hx-trigger': 'change'
	})
    )
	edad = forms.IntegerField()
	acompanantes = forms.IntegerField()
    
	