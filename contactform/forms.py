from django import forms

class contactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'id': 'exampleFormControlTextarea1'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'class':'form-control',
        'id': 'exampleFormControlInput1'
        }
    ))
    message = forms.CharField(max_length=5000,widget=forms.Textarea(
        attrs={
        'class':'form-control',
        'id': 'exampleFormControlTextarea2',
        'rows': '5'
        }
    ))