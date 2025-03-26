from flask import Flask, jsonify, request
from .Server.Motor import Motor  # Updated import path to point to Server directory

app = Flask(__name__)
PWM = Motor()

@app.route('/motor/<direction>', methods=['POST'])
def control_motor(direction):
    if direction == 'forward': # confirmed
        PWM.setMotorModel(1000, 1000, 1000, 1000)
        return jsonify({"status": "Car moving forward"})
    elif direction == 'backward': # confirmed
        PWM.setMotorModel(-1000, -1000, -1000, -1000)
        return jsonify({"status": "Car moving backward"})
    elif direction == 'right': # confirmed
        PWM.setMotorModel(-1000, 1000, 1000, -1000)
        return jsonify({"status": "Car moving right"})
    elif direction == 'left': # confirmed
        PWM.setMotorModel(1000, -1000, -1000, 1000)
        return jsonify({"status": "Car moving left"})
    elif direction == 'rotate_right':
        PWM.setMotorModel(1000, 1000, -1000, -1000)
        return jsonify({"status": "Car rotating right"})
    elif direction == 'rotate_left':
        PWM.setMotorModel(-1000, -1000, 1000, 1000)
        return jsonify({"status": "Car rotating left"})
    elif direction == 'stop': # confirmed
        PWM.setMotorModel(0, 0, 0, 0)
        return jsonify({"status": "Car stopped"})
    else:
        return jsonify({"error": "Invalid direction"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
