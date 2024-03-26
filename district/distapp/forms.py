from django import forms
from .models import District


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = "__all__"

        widgets = {
            "district_name": forms.TextInput(attrs={'class': 'form-control'}),
            "number_of_tehsils": forms.NumberInput(attrs={'class': 'form-control'}),
            "number_of_villages": forms.NumberInput(attrs={'class': 'form-control'}),
            "district_collector": forms.TextInput(attrs={'class': 'form-control'}),
            "famous_spot": forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
