from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8002, host="10.0.19.162")
