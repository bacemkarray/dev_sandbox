from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_text():
    data = request.json
    reversed_string = data["text"][::-1]
    length = len(reversed_string)
    return jsonify({"message": reversed_string, "length": length})




if __name__=='__main__':
    app.run(debug=True)