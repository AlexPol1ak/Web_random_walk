from django import forms

class AmountPoints(forms.Form):
    """Количество  точек """
    points = forms.IntegerField(min_value=1)

class AmountPointsDual(forms.Form):
        """Количество  точек для двух блужданий """

        points = forms.IntegerField(min_value=1)

