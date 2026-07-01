#include <Servo.h>


float PAN_KP = 0.08; 
float PAN_KD = 0.5;

float TILT_KP = 0.08; 
float TILT_KD = 0.5;

float lastPanError = 0;
float lastTiltError = 0;
unsigned long lastUpdate = 0;

Servo panServo;
Servo tiltServo;
int buzzerPin = 12; 

// --- MEMORY ---
unsigned long lastBeatTime = 0;
int heartRate = 800;
int deadband = 10;
int currentPan = 1500;
int currentTilt = 1500;
float targetPan = 1500.0;   
float targetTilt = 1500.0;


class SmoothPID {
  public:
    float kp, kd;
    float lastError;
    
    SmoothPID(float p, float d) {
      kp = p;
      kd = d;
      lastError = 0;
    }

    
    float compute(float target, float current) {
      float error = target - current;
      
      // PROPORTIONAL: "Move towards target"
      float P = error * kp;
      
      // DERIVATIVE: "Whoa, slow down if we are moving too fast!"
      float D = (error - lastError) * kd;
      
      lastError = error;
      
      return P + D;
    }
};



SmoothPID pidPan(PAN_KP, PAN_KD);
SmoothPID pidTilt(TILT_KP, TILT_KD);

void setup() {
  tiltServo.attach(9);
  panServo.attach(10);
  pinMode(buzzerPin, OUTPUT); 
  Serial.begin(9600);
  Serial.setTimeout(10);
  noTone(buzzerPin); 
  panServo.writeMicroseconds(currentPan);
  delay(1000);
  tiltServo.writeMicroseconds(currentTilt);
  delay(500);

}

void loop() {
  if (Serial.available() > 0) {
    

    int p_target = Serial.parseInt(); 
    int t_target = Serial.parseInt(); 
    int f = Serial.parseInt(); 
    
    while (Serial.available() > 0) { Serial.read(); }

    // --- SAFETY CLAMPS ---
    if (p_target < 500) p_target = 500; if (p_target > 2400) p_target = 2400;
    if (t_target < 500) t_target = 800; if (t_target > 2300) t_target = 2200;

    // --- THE DEADBAND FILTER (The Cure for Jitter) ---
    targetPan = p_target;
    targetTilt = t_target;

    if (millis() - lastUpdate > 10) {
      lastUpdate = millis();

      
      float movePan = pidPan.compute(targetPan, currentPan);
      float moveTilt = pidTilt.compute(targetTilt, currentTilt);
      
      // Only move PAN if the change is big enough
      if (abs(p_target - currentPan) > deadband) {
        currentPan += movePan;
        panServo.writeMicroseconds(currentPan);
        //currentPan = p_target; // Remember new position
      }

      // Only move TILT if the change is big enough
      if (abs(t_target - currentTilt) > deadband) {
        currentTilt += moveTilt;
        tiltServo.writeMicroseconds(currentTilt);
        //currentTilt = t_target; // Remember new position
      }

      

      // Heartbeat Logic (Same as before)
      if (f == 1) {
        if (millis() - lastBeatTime >= heartRate) {
          lastBeatTime = millis();
          tone(buzzerPin, 40, 150); 
        }
      } else {
        noTone(buzzerPin);
      }
    }
  }
}


