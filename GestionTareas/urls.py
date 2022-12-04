"""GestionTareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the 'include()' function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from myapp.views import (
    index_view, vista1, vista2, form_view, aula_view,
    formAlum, showAlum, formProf, showProf, NoTemplate,
    TemplateView, Otro
)

from vitrina.views import (
    BookList, BootstrapEj, SelectBook, ViewSession,
    InsertBook, SelectBookTwo, BookAuthor, ListBooks
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view.as_view(), name='index'),
    path('vista1/', vista1.as_view(), name='vista1'),
    path('vista2/', vista2.as_view(), name='vista2'),
    path('form_view/', form_view.as_view(), name='form_view'),
    path('aula_view/<aula>', aula_view.as_view(), name='aula_view'),
    path('formAlum/', formAlum.as_view(), name='formAlum'),
    path('formAlum/<nombre>', showAlum.as_view(), name='showAlum'),
    path('formProf/', formProf.as_view(), name='formProf'),
    path('formProf/<nombre>', showProf.as_view(), name='showProf'),
    path('NoTemplate/', NoTemplate.as_view(), name='NoTemplate'),
    path('TemplateView/', TemplateView.as_view(), name='TemplateView'),
    path('Otro/', Otro.as_view(), name='Otro'),
    # Old book list url, commented for new usage
    # path('booklist/', BookList.as_view(), name='booklist'),
    # New book list url implementation, this implementation is made when is a class-based url, commented for
    # Memcached limitation of 1mb
    path('booklist/', cache_page(60*15)(BookList.as_view()), name='booklist'),
    path('bootstrapej/', BootstrapEj.as_view(), name='bootstrapej'),
    path('SelectBook/<id>', SelectBook.as_view(), name='SelectBook'),
    path('select_book/<id>', SelectBookTwo.as_view(), name='select_book'),
    path('book_author/<id>', BookAuthor.as_view(), name='book_author'),
    path('ViewSession/', ViewSession.as_view(), name='ViewSession'),
    path('InsertBook/', InsertBook.as_view(), name='InsertBook'),
    # Usage of cache_page
    path('ListBooks/', cache_page(60*10)(ListBooks.as_view()), name='ListBooks')
]
