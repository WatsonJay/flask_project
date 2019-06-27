from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 主键
    name = db.Column(db.String(20), nullable=False)  # 名字
    password = db.Column(db.String(40), nullable=False)  # 密码

    def __init__(self, name, password):
        self.name = name
        self.password = password

class Movie(db.Model):  # 表名将会是 movie
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 主键
    title = db.Column(db.String(60), nullable=False)  # 电影标题
    year = db.Column(db.String(4), nullable=False)  # 电影年份

    def __init__(self, title, year):
        self.title = title
        self.year = year
