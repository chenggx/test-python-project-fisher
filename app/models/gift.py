from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import BaseModel, db
from app.models.wish import Wish
from app.spider.yushu_book import YushuBook


class Gift(BaseModel):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False, comment='isbn')
    # 因为图书数据不在数据库，所以下面的字段被注释
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False, comment='是否已经被赠送')

    @classmethod
    def recent(cls):
        return (cls.query.filter_by(launched=False)
                .group_by(cls.isbn)
                .order_by(desc(cls.create_time))
                .limit(30)
                .distinct()
                .all())

    @property
    def book(self):
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_my_gifts(cls, uid):
        return cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """
        获取每个 isbn 所对应的索取者的数量
        :param isbn_list:
        :return:
        """
        count_list = db.session.query(Wish.isbn, func.count(Wish.id)).filter(
            Wish.isbn.in_(isbn_list),
            Wish.status == 1
        ).group_by(Wish.isbn).all()
        # 上面的代码等同于如下 SQL
        # SELECT isbn,count(id) FROM wish WHERE status = 1 and isbn in('9787806579060','9787101028584') GROUP by isbn;

        return [{'isbn': w[0], 'count': w[1]} for w in count_list]
