class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource')

    def query(self):
        print('query work ')


with MyResource() as m:
    m.query()

# 同上面一样的效果
from contextlib import contextmanager


class OtherResource:
    def query(self):
        print('query work')


@contextmanager
def make_other_resource():
    print('connect to resource')
    yield OtherResource()
    print('close resource')


with make_other_resource() as ot:
    ot.query()


# contextmanager 使用技巧
@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print('红楼梦', end='')
