from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='../static') # static_folder indica o local onde o diretorio static esta
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
#debug = True refresh automaticaly
#port define port number