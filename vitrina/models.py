from django.db import models


class Books(models.Model):
    title = models.TextField()
    authors = models.TextField()
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.BigIntegerField()
    text_reviews_count = models.BigIntegerField()
    publication_date = models.DateField(auto_now=True)
    publisher = models.TextField()

    def __str__(self):
        return self.title

    def to_json(self):
        book_in_json = {
            'title': self.title,
            'authors': self.authors,
            'average_rating': self.average_rating,
            'isbn': self.isbn,
            'isbn13': self.isbn13,
            'language_code': self.language_code,
            'num_pages': self.num_pages,
            'ratings_count': self.ratings_count,
            'text_reviews_count': self.text_reviews_count,
            'publication_date': str(self.publication_date),
            'publisher': self.publisher
        }

        return book_in_json
