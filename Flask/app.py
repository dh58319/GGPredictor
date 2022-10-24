from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/Crawling')
def Crawling():
    return render_template('Crawling.html')

@app.route('/Preprocessing')
def Preprocessing():
    return render_template('Preprocessing.html')

@app.route('/LSA')
def LSA():
    return render_template('LSA.html')

@app.route('/Apriori')
def Apriori():
    return render_template('Apriori.html')

@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')


if __name__ == '__main__':
    app.run()