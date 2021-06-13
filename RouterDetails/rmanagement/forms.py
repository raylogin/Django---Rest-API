from django import forms

class FormName(forms.Form):
    sapid = forms.CharField()
    hostname = forms.CharField()
    loopback = forms.CharField()
    macaddress = forms.CharField()

class FormName_delete(forms.Form):
    sapid = forms.CharField()

class FormName_generate(forms.Form):
    num = forms.IntegerField()