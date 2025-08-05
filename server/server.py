from flask import Flask, request, jsonify, render_template
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return render_template("app.html")

@app.route('/similarity', methods=['POST', 'OPTIONS'])
def similarity():
    print("=== SIMILARITY REQUEST DEBUG ===")
    print(f"Request method: {request.method}")
    print(f"Request files: {request.files}")
    print(f"Request form: {request.form}")
    print(f"Content type: {request.content_type}")
    
    if 'image' not in request.files:
        print("ERROR: No 'image' key in request.files")
        return jsonify({'error': 'No image file provided'}), 400
    
    image = request.files['image']
    print(f"Image filename: {image.filename}")
    print(f"Image content type: {image.content_type}")
    
    if image.filename == '':
        print("ERROR: Empty filename")
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        result = util.similarity(image)
        print(f"Similarity result: {result}")
        print(f"Returning JSON: {result}")
        return jsonify(result)
    except Exception as e:
        print(f"ERROR in similarity: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/classify', methods=['POST', 'OPTIONS'])
def classify_image():
    print("=== CLASSIFY REQUEST DEBUG ===")
    print(f"Request method: {request.method}")
    print(f"Request files: {request.files}")
    print(f"Request form: {request.form}")
    print(f"Content type: {request.content_type}")
    
    if 'image' not in request.files:
        print("ERROR: No 'image' key in request.files")
        return jsonify({'error': 'No image file provided'}), 400
    
    image = request.files['image']
    print(f"Image filename: {image.filename}")
    print(f"Image content type: {image.content_type}")
    
    if image.filename == '':
        print("ERROR: Empty filename")
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        result = util.classify_image(image)
        print(f"Classification result: {result}")
        response_data = {'result': str(result)}
        print(f"Returning JSON: {response_data}")
        return jsonify(response_data)
    except Exception as e:
        print(f"ERROR in classify: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print('Starting Python Flask server...')
    util.load_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)