import www.orm as orm
from www.models import User, Blog, Comment


def test():
    orm.create_pool(user='root', password='ting876587134', db="awesome")
    user = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from user.save()


for x in test():
    pass
