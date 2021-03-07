from django import forms
from .models import Book
from .models import Reference

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('page','remarks',)

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        exclude = ('remarks_ref',) 