from vitrina.models import Books


def check_author_session(id, authors):
    book = Books.objects.get(pk=id)
    if book.authors == authors:
        return True
    else:
        return False
