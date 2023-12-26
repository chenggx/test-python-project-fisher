from sqlalchemy import Column, String, Boolean, Float, Integer

from app.models.base import db, BaseModel
from werkzeug.security import generate_password_hash


class User(BaseModel):
    id = Column(db.Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(256))
    confirmed = Column(Boolean, default=False, comment='')
    beans = Column(Float, default=0, comment='')
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
