from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from vitrina.models import Books
from vitrina.forms import BookInsert


class BookList(ListView):
    model = Books
    template_name = 'booklist.html'


class SelectBook(View):
    def get(self, request, id):
        book = Books.objects.filter(pk=id).first()

        if book:
            nombre = 'hola'
            request.session['title'] = book.title
            request.session['authors'] = book.authors

            request.session[nombre] = book.toJson()
            valor = request.session[nombre]

            context = {'book': book}

            # return render(request, 'SelectBook.html', context)
            return HttpResponse(f'Los datos del libro son: {book}. Y el dato es: {valor}')
        else:
            return HttpResponse(f'No se encontro el libro especificado')


class InsertBook(View):
    def get(self, request):
        bookInsert = BookInsert()

        context = {'form': bookInsert}

        return render(request, 'InsertBook.html', context)

    def post(self, request):
        formulario = BookInsert(request.POST)
        if formulario.is_valid():
            request.session['title_insert'] = formulario.cleaned_data['title']
            request.session['authors_insert'] = formulario.cleaned_data['authors']

            return HttpResponse('Valores guardados en sesion')
        return HttpResponse('Valores del formulario invalidos')


class ViewSession(View):
    def get(self, request):
        # title = request.session['title']
        # authors = request.session['authors']
        titleI = request.session['title_insert']
        authorsI = request.session['authors_insert']

        # return HttpResponse(f'El libro en sesion es: {title}, y los autores son: {authors}.')
        return HttpResponse(f'El libro guardado en sesion es: {titleI} y los autores son: {authorsI}')


class BootstrapEj(View):
    def get(self, request):
        return render(request, 'ejemplo_bootstrap.html')
