from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')