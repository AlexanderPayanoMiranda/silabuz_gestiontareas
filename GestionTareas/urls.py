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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from myapp.views import (
    index_view, vista1, vista2, form_view, aula_view,
    formAlum, showAlum, formProf, showProf, NoTemplate,
    TemplateExample, Otro, TemplateView
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
    path('TemplateExample/', TemplateExample.as_view(), name='TemplateExample'),
    path('Otro/', Otro.as_view(), name='Otro'),
    path('TemplateView/', TemplateView.as_view(), name='TemplateView')
]
