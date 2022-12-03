from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from myapp.forms import InputForm, AlumnoForm, ProfesorForm


from datetime import datetime
from dateutil.relativedelta import relativedelta


class index_view(View):
    template_get = 'index.html'

    def get(self, request):
        context = {'name': 'Alex'}
        return render(request, self.template_get, context)

    def post(self, request):
        return HttpResponse('Soy POST de index_view')


class vista1(View):
    template_get = 'vista1.html'

    def get(self, request):
        fecha_nacimiento = datetime.strptime("18/5/1997", "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)

        context = {}
        context['name'] = 'Alex'
        context['edad'] = edad.years

        return render(request, self.template_get, context)


class vista2(View):
    template_get = 'vista2.html'

    def get(self, request):
        lista = [1, 2, 3, 4, 5]
        context = {
            'name': 'Alex',
            'list': lista
        }

        return render(request, self.template_get, context)


class form_view(View):
    template_get = 'form.html'
    template_post = 'Hola soy POST de form_view'

    def get(self, request):
        formulario = InputForm()
        context = {'form': formulario}

        return render(request, self.template_get, context)

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            request.session['hora_entrada'] = str(form.cleaned_data['hora_entrada'])

            return redirect('aula_view', aula=form.cleaned_data['aula'])


class aula_view(View):
    def get(self, request, aula):
        hora = request.session['hora_entrada']

        return HttpResponse(f'El salon es: {aula}, y la hora es: {hora}')


class formAlum(View):
    template_get = 'formAlum.html'

    def get(self, request):
        context = {}
        context['form'] = AlumnoForm()

        return render(request, self.template_get, context)

    def post(self, request):
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            request.session['apellido'] = formulario.cleaned_data['last_name']
            request.session['id_aula'] = formulario.cleaned_data['id_aula']

            return redirect('showAlum', nombre=formulario.cleaned_data['first_name'])


class showAlum(View):
    def get(self, request, nombre):
        apellido = request.session['apellido']
        id_aula = request.session['id_aula']

        return HttpResponse(f'El nombre del alumno es: {nombre} {apellido} y  su aula es: {id_aula}')


class formProf(View):
    template_get = 'formProf.html'

    def get(self, request):
        context = {}
        context['form'] = ProfesorForm()

        return render(request, self.template_get, context)

    def post(self, request):
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            request.session['apellido'] = formulario.cleaned_data['last_name']
            request.session['salario'] = str(formulario.cleaned_data['salario'])

            return redirect('showProf', nombre=formulario.cleaned_data['first_name'])


class showProf(View):
    def get(self, request, nombre):
        apellido = request.session['apellido']
        salario = request.session['salario']

        return HttpResponse(f'El nombre del profesor es: {nombre} {apellido} y  su salario es: {salario}')


class NoTemplate(View):
    def get(self, request):
        response = """
            <html>
                <body>
                    <h1>Yo soy NoTemplate</h1>
                </body>
            </html>
        """

        return HttpResponse(response)


class TemplateView(View):
    def get(self, request):
        context = {
            'title': 'harry potter',
            'list': [1, 2, 3, 4, 5],
            'diccionario': {
                'first_name': 'pablo',
                'last_name': 'santivañez'
            }
        }

        return render(request, 'TemplateView.html', context)


class Otro(View):
    def get(self, request):
        return render(request, 'otro.html')