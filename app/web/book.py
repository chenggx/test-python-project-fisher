import json

from flask import jsonify, request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from . import web
from ..forms.book import SearchForm
from ..view_models.book import BookViewModel, BookCollection


@web.route('/book/search')
def search():
    """
    :param q: 查询关键字
    :param page: 分页
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if not form.validate():
        return render_template('search.html', books=books)

    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    yushu_book = YushuBook()

    if isbn_or_key == 'isbn':
        yushu_book.search_by_isbn(q)
    else:
        yushu_book.search_by_title(q, page)

    books.fill(yushu_book, q)

    # return json.dumps(books, default=lambda o: o.__dict__)
    return render_template('search_result.html', books=books,keyword=q)
