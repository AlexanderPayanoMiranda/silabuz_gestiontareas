from django import forms


class BookInsert(forms.Form):
    title = forms.CharField(max_length=50)
    authors = forms.CharField(max_length=50)


class InputForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()


class BookForm(forms.Form):
    title = forms.CharField(max_length=1000)
    authors = forms.CharField(max_length=1000)
    average_rating = forms.FloatField()
    isbn = forms.CharField(max_length=10)
    isbn13 = forms.CharField(max_length=13)
    language_code = forms.CharField(max_length=10)
    num_pages = forms.IntegerField()
    ratings_count = forms.IntegerField()
    text_reviews_count = forms.IntegerField()
    publication_date = forms.DateField()
    publisher = forms.CharField(max_length=1000)
