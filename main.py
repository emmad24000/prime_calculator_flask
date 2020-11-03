from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
n = 0
@app.route('/')
def fx():

    return render_template('home.html')
@app.route('/isPrime/<n>')
def isPrime(n):
    isPrime = " is Prime."
    for i in range(2, int(n)):
        if int(n) % i == 0:
            isPrime = " is not Prime."
    return render_template('isPrime.html', n=int(n), isPrime=isPrime)

@app.route('/<n>')
def back(n):
    return render_template('home.html')

app.run(debug=True)