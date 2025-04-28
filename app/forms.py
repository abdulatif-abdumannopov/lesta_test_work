from django import forms
import os
from app.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document']
        widgets = {
            "document": forms.FileInput(attrs={
                'class': 'file_input',
            }),
        }

    def clean_document(self):
        document = self.cleaned_data.get('document')
        if document:
            ext = os.path.splitext(document.name)[1].lower()
            if ext != '.txt':
                raise forms.ValidationError('Only .txt files are allowed.')
        return document