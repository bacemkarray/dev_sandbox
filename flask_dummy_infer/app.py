# Flask starter:
# - Use @app.route to map URL to functions
# - Use request.json to get POST data
# - Use jsonify() to return JSON
# Copy this file when starting a new Flask project

from flask import Flask, request, jsonify

app = Flask(__name__) #__name__ is a special variable that tells Python whether the current file is the main program or just a module.
#Flask uses it to know where it is and whether it should run.

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data["message"]})

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    required_keys = ['op', 'a', 'b']
    if not all(k in data for k in required_keys):
        return jsonify({"error": "Missing Parameters"})
    
    operations = {"add": lambda a,b: a+b,
                  "subtract": lambda a,b: a-b,
                  "multiply": lambda a,b: a*b,
                  "divide": lambda a,b: a/b if b != 0 else "error"
    }

    op_func = operations.get(data['op'])
    result = op_func(data['a'], data['b'])
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)