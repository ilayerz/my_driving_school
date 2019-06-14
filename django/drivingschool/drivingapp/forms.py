from django import forms

class PlanningForm(forms.Form):
	date = forms.CharField(label="date",max_length=100, widget=forms.DateInput(attrs={'class': 'datepicker'}))
	lieu = forms.CharField(label="lieu", max_length=100)
