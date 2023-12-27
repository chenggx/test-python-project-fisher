from sqlalchemy import Column, String, Boolean, Float, Integer

from .base import db, BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .gift import Gift
from .wish import Wish
from ..libs.helper import is_isbn_or_key
from ..spider.yushu_book import YushuBook


class User(UserMixin, BaseModel):
    id = Column(db.Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(256))
    confirmed = Column(Boolean, default=False, comment='')
    beans = Column(Float, default=0, comment='鱼豆')
    send_counter = Column(Integer, default=0, comment='')
    receive_counter = Column(Integer, default=0, comment='')
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd_raw):
        self._password = generate_password_hash(pwd_raw)

    def check_password(self, pwd_raw):
        return check_password_hash(self._password, pwd_raw)

    def can_save_to_list(self, isbn):
        # 不是 isbn
        if is_isbn_or_key(isbn) != 'isbn':
            return False

        # 系统中没有这本书
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(isbn)
        if not YushuBook.first:
            return False

        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不能同时称为赠书者和索要者
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # 既不在赠送清单中，也不在心愿清单中才能添加
        if not gifting and not wishing:
            return True
        else:
            return False
