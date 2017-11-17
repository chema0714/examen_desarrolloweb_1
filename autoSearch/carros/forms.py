from django import forms

from .models import Car

class CarModelForm(forms.ModelForm):
    Type = forms.CharField(label='',
                              widget=forms.Textarea(
                                        attrs={'placeholder':"tipo",
                                               'class': "textarea"}
                              ))

    class Meta:
        model = Car
        fields = [
            "make",
            "Type",
            "year",
            "colour",
            "price",
            "created"
        ]