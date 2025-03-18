from django import forms
from .models import Word, Varna, Source, Type
import json

class WordForm(forms.ModelForm):
    synonyms = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter synonyms separated by commas'}),
        required=False
    )
    example = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=False
    )
    nature = forms.ChoiceField(
        choices=[('', '---------'), ('সকর্মক', 'সকর্মক'), ('অকর্মক', 'অকর্মক')],
        required=False
    )
    past = forms.CharField(required=False)
    present = forms.CharField(required=False)
    future = forms.CharField(required=False)
    label = forms.CharField(required=False)  # Added for label
    origin = forms.CharField(required=False)  # Added for origin

    class Meta:
        model = Word
        fields = ['varna', 'source', 'type', 'root_word']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If editing an existing instance, prepopulate fields from details
        if self.instance and self.instance.pk and self.instance.details:
            details = self.instance.details
            self.fields['label'].initial = details.get('label', '')
            self.fields['origin'].initial = details.get('origin', '')
            self.fields['example'].initial = details.get('example', '')
            self.fields['synonyms'].initial = ', '.join(details.get('synonyms', []))
            if self.instance.type.type_name == 'ক্রিয়া':
                self.fields['nature'].initial = details.get('nature', '')
                tense = details.get('tense', {})
                self.fields['past'].initial = tense.get('past', '')
                self.fields['present'].initial = tense.get('present', '')
                self.fields['future'].initial = tense.get('future', '')

    def clean(self):
        cleaned_data = super().clean()
        # Construct the details JSON from form fields
        details = {
            'label': cleaned_data.get('label', ''),
            'origin': cleaned_data.get('origin', ''),
            'example': cleaned_data.get('example', ''),
            'synonyms': [s.strip() for s in cleaned_data.get('synonyms', '').split(',') if s.strip()]
        }
        if cleaned_data.get('type') and cleaned_data['type'].type_name == 'ক্রিয়া':
            details['nature'] = cleaned_data.get('nature')
            details['tense'] = {
                'past': cleaned_data.get('past', ''),
                'present': cleaned_data.get('present', ''),
                'future': cleaned_data.get('future', '')
            }
        # Assign the constructed details to the cleaned_data
        cleaned_data['details'] = details
        return cleaned_data