from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def handle_calculate():
    data = request.get_json()
    result = calculate(data['expression'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
