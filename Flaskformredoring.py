from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_days', methods=['POST'])
def calculate_days():
    age = int(request.form['age'])
    days = age * 365
    res=""
    return render_template('result.html', days=days)

if __name__ == '__main__':
    app.run(debug=True)