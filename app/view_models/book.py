class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher'],
        self.pages = book['pages'] or '',
        self.image = book['image'],
        self.summary = book['summary'] or '',
        self.author = '、'.join(book['author'])


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

# class _BookViewModel:
#     @classmethod
#     def package_single(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = [cls._cut_book_data(data)]
#         return returned
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls._cut_book_data(book) for book in data['books']]
#         return returned
#
#     @classmethod
#     def _cut_book_data(cls, data):
#         book = {
#             'title': data['title'],
#             'publisher': data['publisher'],
#             'pages': data['pages'] or '',
#             'image': data['image'],
#             'summary': data['summary'] or '',
#             'author': '、'.join(data['author'])
#         }
#         return book
