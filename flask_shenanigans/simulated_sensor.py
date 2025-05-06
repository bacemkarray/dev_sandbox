from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data_log = []

@app.route('/sensor', methods=["POST"])
def motion_sensor():
    data = request.get_json()
    sensor_data_log.append(data)

    if data["motion_level"] > 0.5:
        alert = "high"
    else:
        alert = "low"

    return jsonify({"alert": alert})



@app.route('/dashboard', methods=["GET"])
def motion_history():
    return jsonify(sensor_data_log)



if __name__=='__main__':
    app.run(debug=True)