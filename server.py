from flask import Flask, request, jsonify
import serial
import time
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os
from flask import Flask, send_from_directory









app = Flask(__name__)



CORS(app) 

ARDUINO_PORT = 'COM4'  # Update if your port changes
BAUD_RATE = 9600
try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    print(f"✅ [HARDWARE] Connected to Arduino on {ARDUINO_PORT}")
except Exception as e:
    print(f"⚠️ [HARDWARE ERROR] Could not connect to Arduino: {e}")
    arduino = None


socketio = SocketIO(app, cors_allowed_origins="*") 



@socketio.on('neck_movement')
def handle_neck(data):
    pan = data.get('pan', 1500)
    tilt = data.get('tilt', 1500)
    
    # Map the 0-180 degree angles to 544-2400 microseconds for the Arduino 
    #pan_us = int((pan - 0) * (2400 - 544) / (180 - 0) + 544)
    #tilt_us = int((tilt - 0) * (2400 - 544) / (180 - 0) + 544)
    print(f"[matrix vision]  pan:{pan}  ;;  tilt:{tilt} " )
    #print(f"tilt:")
    #print(tilt)
    
    if arduino:
        #  the string exactly be as index.html did: tilt,pan,fire
        
        command = f"{pan},{tilt},0\n"
        try:
            arduino.write(command.encode('utf-8'))
        except Exception as e:
            print(f"⚠️ [SERIAL ERROR]: {e}")




            







if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5050, debug=True, use_reloader=False)



