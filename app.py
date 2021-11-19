from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return('Hello World')

@app.route('/Walrus')
def sea_creature():
    return('Hello Walrus')

if __name__ == '__main__':
    app.run(debug=True)
