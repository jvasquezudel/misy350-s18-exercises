from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('template.html')

@app.route('/user/<string:username>')
def username(username):
    return "<h1>hello %s</h1>" % username


if __name__ == '__main__':
    app.run()
