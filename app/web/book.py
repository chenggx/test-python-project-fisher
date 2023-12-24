from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from . import web
from ..forms.book import SearchForm


@web.route('/book/search')
def search():
    """
    :param q: 查询关键字
    :param page: 分页
    :return:
    """
    form = SearchForm(request.args)
    if not form.validate():
        return jsonify({'code': 400, 'msg': form.errors})
    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YushuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_title(q, page)
    return jsonify(result)
