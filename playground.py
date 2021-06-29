from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ("index.html")

@app.route('/play')
def play():
    return render_template ("index.html")

@app.route('/play/<num>/green')
def green(num):
    return render_template ("green.html", num = int(*num))

@app.route('/play/<num>')
def boxes(num):
    return render_template ("num.html", num = int(num))

if __name__ == "__main__":

    app.run(debug=True)
