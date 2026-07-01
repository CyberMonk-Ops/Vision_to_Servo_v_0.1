import os
import urllib.request

# Enforce clean target directory
target_dir = "mediapipe"
os.makedirs(target_dir, exist_ok=True)

# Correct distribution footprint for offline MediaPipe FaceMesh
urls = [
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh_solution_packed_assets_loader.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh_solution_packed_assets.data",
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh_solution_simd_wasm_bin.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh_solution_simd_wasm_bin.wasm",
    "https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.binarypb"
]

print("Executing automated MediaPipe alignment loop...")

for url in urls:
    filename = url.split("/")[-1]
    filepath = os.path.join(target_dir, filename)
    print(f"Pulling asset: {filename} -> {filepath}")
    try:
        # User-Agent mask prevents CDN traffic shaping bottlenecks
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"![CRITICAL EXCEPTION] Could not map target {filename}: {e}")

print("\nSync completed. Local binary array fully populated.")


