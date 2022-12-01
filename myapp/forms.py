from django import forms


class InputForm(forms.Form):
    aula = forms.CharField(max_length=2)
    hora_entrada = forms.TimeField(
        help_text='Ingresa la hora en formato HH:MM'
    )


class AlumnoForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    id_aula = forms.IntegerField()


class ProfesorForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    salario = forms.FloatField()
