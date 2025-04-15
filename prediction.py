
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        a = float(request.args.get('a', 0))
    except ValueError:
        a = 0
    try:
        b = float(request.args.get('b', 0))
    except ValueError:
        b = 0

    # decyzja
    result = 1 if (a + b) > 5.8 else 0

    # JSON
    return jsonify({
        "prediction": result,
        "features": {"a": a, "b": b}
    })

if __name__ == '__main__':
    app.run()
