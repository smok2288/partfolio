from django import forms


CHOICE_QUATITY=[(i, str(i)) for i in range(1, 10)]

class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICE_QUATITY, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    