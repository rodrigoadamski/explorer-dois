from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['titulo', 'descricao', 'localizacao', 'foto', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: -23.55,-46.63'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
