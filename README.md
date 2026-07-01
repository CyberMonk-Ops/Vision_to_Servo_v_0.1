# Vision Tracker to Servo Movement

An offline, zero-latency computer vision tracking solution that interfaces browser-native machine learning pipelines with physical servo controls over high-performance WebSocket arrays. 

Using MediaPipe FaceMesh processing loops, the system calculates relative coordinates, implements spatial filtering (smoothing/deadbands), and stream-telemeterizes real-time position vectors to control target hardware positioning systems.

---

## System Architecture

```text
[Webcam Stream] ---> [MediaPipe WASM Engine] ---> [HUD Tracking Matrix]
                                                          |
                                                 (Deadband / Smoothing)
                                                          |
[Hardware Control Server] <--- [Socket.IO Link] <--- [Telemetry Output]




Prerequisites
Before configuring the codebase, ensure you have an active Python runtime environment and an isolated virtual wrapper ready:
Python 3.10 or higher
Modern web browser with WebGL 2.0 interface validation enabled
Installation & Environment Assembly


Clone the project assets to your local machine:

git clone [https://github.com/CyberMonk-Ops/Vision_to_Servo_v_0.1?tab=readme-ov-file](https://github.com/CyberMonk-Ops/Vision_to_Servo_v_0.1?tab=readme-ov-file)
cd your-repository-name



Initialize your local virtual architecture and apply the dependency matrices:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt


Critical Step: Run the Asset Synchronization Script
To keep the codebase lightweight and eliminate network cross-origin resource limitations (CORS), the core WebAssembly compilation wrappers and packed graph asset structures are excluded from version control. Pull down the runtime files locally by firing the automated delivery script:

python download_assets.py


Execution Flow

Spin up your hardware communication server platform:

python server.py

Serve your static control panel tracking loop through a local port mapping loop (e.g., via your server configuration or a basic web utility) and target http://localhost:8000.

Authorize hardware camera accessibility inside the browser. The system will cleanly initialize the local binary configurations, isolate facial bounding perimeters, and activate the servo coordinate array updates.


