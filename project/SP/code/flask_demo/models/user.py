from exts import db


class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义列对象
    id = db.Column(db.INT, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    # # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    # def __repr__(self):
    #     return '<User {}> '.format(self.username)