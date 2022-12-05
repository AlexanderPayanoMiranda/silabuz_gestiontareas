from django import forms


class BookInsert(forms.Form):
    title = forms.CharField(max_length=50)
    authors = forms.CharField(max_length=50)


class InputForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
