from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('blog.html')

@app.route('/contacts/')
def contact():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()