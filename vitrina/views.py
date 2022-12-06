from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.conf import settings

from vitrina.tasks import send_book
from vitrina.models import Books
from vitrina.forms import BookInsert, InputForm, BookForm
from vitrina import utils


class BookList(ListView):
    model = Books
    template_name = 'booklist.html'
    # Added query to limit amount of results
    queryset = Books.objects.filter()[:30]


class SelectBook(View):
    def get(self, request, id):
        book = Books.objects.filter(pk=id).first()

        if book:
            nombre = 'hola'
            request.session['title'] = book.title
            request.session['authors'] = book.authors

            request.session[nombre] = book.to_json()
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


# This class is created instead of select_book that is shown in the workshop guide of caches
class SelectBookTwo(View):
    def get(self, request, id):
        book = Books.objects.filter(pk=id).first()

        request.session['authors'] = book.authors
        request.session['id'] = id

        context = {
            'book_id': id,
            'book': book.to_json(),
            'form': InputForm()
        }

        return render(request, 'oneBook.html', context)

    def post(self, request, id):
        form = InputForm(request.POST)
        if form.is_valid():
            send_book.delay(form.cleaned_data['nombre'], form.cleaned_data['email'])
            # send_book.apply_async(args=[form.cleaned_data['nombre'], form.cleaned_data['email']])

            # send_mail(
            #     'Subject',
            #     'Here is your book ' + form.cleaned_data['nombre'],
            #     settings.EMAIL_HOST_USER,
            #     [form.cleaned_data['email']],
            #     fail_silently=False
            # )

            return HttpResponse(form.cleaned_data['nombre'] + " " + form.cleaned_data['email'])


class BookAuthor(View):
    def get(self, request, id):
        context = {
            'authors': request.session['authors']
        }

        if utils.check_author_session(id, context['authors']):
            return render(request, 'author.html', context)
        else:
            context = {
                'authors': 'El autor no se encuentra guardado en la sesion.'
            }
            return render(request, 'author.html', context)


class ListBooks(ListView):
    model = Books
    template_name = 'ListBooks.html'
    # Added query to limit amount of results
    queryset = Books.objects.filter()[:10]


class UpdateBook(View):
    def get(self, request, id):
        book = Books.objects.filter(pk=id).first()

        form = BookForm(initial={
            'title': book.title,
            'authors': book.authors,
            'average_rating': book.average_rating,
            'isbn': book.isbn,
            'isbn13': book.isbn13,
            'language_code': book.language_code,
            'num_pages': book.num_pages,
            'ratings_count': book.ratings_count,
            'text_reviews_count': book.text_reviews_count,
            'publication_date': book.publication_date,
            'publisher': book.publisher,
        })

        context = {
            'form': form
        }

        return render(request, 'UpdateBook.html', context)

    def post(self, request, id):
        form = BookForm(request.POST)
        if form.is_valid():
            book = Books.objects.filter(pk=id).first()

            book.title = form.cleaned_data['title']
            book.authors = form.cleaned_data['authors']
            book.average_rating = form.cleaned_data['average_rating']
            book.isbn = form.cleaned_data['isbn']
            book.isbn13 = form.cleaned_data['isbn13']
            book.language_code = form.cleaned_data['language_code']
            book.num_pages = form.cleaned_data['num_pages']
            book.ratings_count = form.cleaned_data['ratings_count']
            book.text_reviews_count = form.cleaned_data['text_reviews_count']
            book.publication_date = form.cleaned_data['publication_date']
            book.publisher = form.cleaned_data['publisher']

            book.save()

            return HttpResponse('Book updated successfully!')
        return HttpResponse('Book was not updated!')
