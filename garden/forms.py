from django import forms

from .models import Gul,Turlar


class GulForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Gul nomi",
        'class': "form-control"
    }))
    info = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Gul haqida malumot",
        'class': "form-control",
        "rows": 3
    }))
    photo = forms.ImageField(required=False, widget=forms.FileInput())
    turi = forms.ModelChoiceField(queryset=Turlar.objects.all(),
                                      widget=forms.Select(attrs={
                                          "class": "form-select"
                                      }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
        "checked": "checked"
    }))
    video = forms.FileField(required=False, widget=forms.FileInput())

    def create(self):
        gul = Gul.objects.create(**self.cleaned_data)
        return gul