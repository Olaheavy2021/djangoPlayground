from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput
        (attrs={'class': 'form-control form-control-lg'}))
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control form-control-lg'}))
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput
        (attrs={'class': 'form-control form-control-lg'}))
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
        (attrs={'class': 'form-control form-control-lg', 'rows': '4'}))