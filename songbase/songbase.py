from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form-basics')
def form_basics():
    return render_template('form-basics.html')

@app.route('/form-demo')
def form_demo():
    first_name = request.args.get('first_name')
    return first_name


@app.route('/user')
def user():
    return '<h1> The page for the users </h1>'

@app.route('/user/<string:username>')
def username(username):
    return render_template('template.html', username = username)


if __name__ == '__main__':
    app.run()
