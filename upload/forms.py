from django import forms
from .models import Document


"""
[] import xml parse script
[] write a new class "class Xmlform(forms.Form):"
[] in class generate a new form field for earch vulnerbility item
[] present dynamic form fields in "text.html" with "{{ form }}"
[] bind dynamic model to each dynamic vulnerability form field
"""


class CategorizeForm(forms.Form):
    """subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    key = forms.CharField(max_length=100)
    newquestion = forms.CharField(max_length=100)
    newquestion_answer = forms.CharField(max_length=100)"""
    datafield = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )
