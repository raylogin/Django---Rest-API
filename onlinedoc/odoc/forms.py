from django import forms

class DocForm(forms.Form):
    Filename = forms.CharField()
    # File = forms.CharField(widget=forms.Textarea(attrs={"rows":30, "cols":185, "style":"border: 0.5px solid #555555"}))