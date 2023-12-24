from flask import current_app

from app.libs.httper import HTTP


class YushuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        return HTTP.get(url)

    @classmethod
    def search_by_title(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        return HTTP.get(url)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
