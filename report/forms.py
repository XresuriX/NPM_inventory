from django import forms
from .models import Ingredients, Report


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'discription']


class ReportUpdateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['opening_bgs', 'opening_kgs', 'recieved', 'bags_used_bin', 'bags_used_Th3', 'kgs_used_Th3',
                  'lot_number', 'current_bgs', 'current_kgs', 'total_used_kgs', 'expiry_date']
