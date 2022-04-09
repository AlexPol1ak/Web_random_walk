from django import forms

class AmountPoints(forms.Form):
    """Количество  точек """

    points = forms.IntegerField(min_value=1)