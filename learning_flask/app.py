from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import  SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:@127.0.0.1:3306/test?charset=utf8'

#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据

db = SQLAlchemy(app)
import models
name = 'jaywatson'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Soci cccety', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
@app.route('/hello')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello_world'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

@app.route('/film')
def index():
    return render_template('test.html', name=name, movies=movies)

@app.route('/movie')
def show_all():
   return render_template('movieAdd.html', movies = models.Movie.query.all(), user=name)

@app.route('/movie/add/',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        p_title = request.form.get('title',None)
        p_year = request.form.get('year',None)

        if not p_title or not p_year:
            return 'input error'

        newobj = models.Movie(title=p_title, year=p_year)
        db.session.add(newobj)
        db.session.commit()
        Movies = models.Movie.query.all()
        return redirect(url_for('show_all'))
    Movies = models.Movie.query.all()
    return render_template('movieAdd.html',admins=Movies, user=name)

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html', user=name), 404  # 返回模板和状态码

if __name__ == '__main__':
    app.run(debug=True)
