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