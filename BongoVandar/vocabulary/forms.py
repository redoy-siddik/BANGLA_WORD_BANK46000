from django import forms
from .models import Word, Varna, Source, Type

class WordForm(forms.ModelForm):
    synonyms = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter synonyms separated by commas'}),
        required=False
    )
    example = forms.CharField(widget=forms.Textarea, required=False)
    nature = forms.ChoiceField(
        choices=[('', '---------'), ('সকর্মক', 'সকর্মক'), ('অকর্মক', 'অকর্মক')],
        required=False
    )
    past = forms.CharField(required=False)
    present = forms.CharField(required=False)
    future = forms.CharField(required=False)

    class Meta:
        model = Word
        fields = ['varna', 'source', 'type', 'root_word', 'details']

    def clean(self):
        cleaned_data = super().clean()
        details = {
            'label': cleaned_data.get('details', {}).get('label', ''),
            'origin': cleaned_data.get('details', {}).get('origin', ''),
            'example': cleaned_data.get('example', ''),
            'synonyms': [s.strip() for s in cleaned_data.get('synonyms', '').split(',') if s.strip()]
        }
        if cleaned_data.get('type') and cleaned_data['type'].type_name == 'ক্রিয়া':
            details['nature'] = cleaned_data.get('nature')
            details['tense'] = {
                'past': cleaned_data.get('past'),
                'present': cleaned_data.get('present'),
                'future': cleaned_data.get('future')
            }
        cleaned_data['details'] = details
        return cleaned_data