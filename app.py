from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/<int:test_int>', methods=['GET'])
def api(test_int):
    return jsonify({'message': test_int})
