import joblib
import json
import face_recognition
import numpy as np
from PIL import Image
import io

__men_model = None
__men_dict = {}
__women_model = None
__women_dict = {}

def face_encode(image):
    """
    Handle both file paths (strings) and Flask FileStorage objects
    """
    print(f"=== FACE_ENCODE DEBUG ===")
    print(f"Image type: {type(image)}")
    print(f"Image: {image}")
    
    if isinstance(image, str):
        # If it's a file path (string)
        print("Processing as file path")
        file = face_recognition.load_image_file(image)
    else:
        # If it's a Flask FileStorage object
        print("Processing as FileStorage object")
        # Read the file content as bytes
        image_bytes = image.read()
        print(f"Read {len(image_bytes)} bytes")
        # Reset file pointer in case it's needed again
        image.seek(0)
        # Convert bytes to PIL Image
        pil_image = Image.open(io.BytesIO(image_bytes))
        print(f"PIL Image size: {pil_image.size}, mode: {pil_image.mode}")
        # Convert PIL Image to numpy array (RGB format)
        file = np.array(pil_image)
        print(f"Numpy array shape: {file.shape}")
        # If image is RGBA, convert to RGB
        if file.shape[2] == 4:
            file = file[:, :, :3]
            print("Converted RGBA to RGB")
    
    print("Calling face_recognition.face_encodings...")
    encode = face_recognition.face_encodings(file)
    print(f"Found {len(encode)} face encodings")
    
    if len(encode) == 0:
        raise ValueError("No face found in the image")
    
    return encode

def classify_image(img):
    try:
        label_dict_men = {a: b for b, a in __men_dict.items()}
        label_dict_women = {a: b for b, a in __women_dict.items()}
        
        encode = face_encode(img)
        
        pred_men = __men_model.predict([encode[0]])[0]
        proba_men = __men_model.predict_proba([encode[0]])
        pred_women = __women_model.predict([encode[0]])[0]
        proba_women = __women_model.predict_proba([encode[0]])
        
        if np.max(proba_men) > np.max(proba_women):
            result = label_dict_men[pred_men]
            confidence = f"{round(np.max(proba_men) * 100, 2)}%"
            return f"{result} (Confidence: {confidence})"
        else:
            result = label_dict_women[pred_women]
            confidence = f"{round(np.max(proba_women) * 100, 2)}%"
            return f"{result} (Confidence: {confidence})"
            
    except Exception as e:
        raise Exception(f"Classification error: {str(e)}")

def similarity(img):
    try:
        label_dict_men = {a: b for b, a in __men_dict.items()}
        label_dict_women = {a: b for b, a in __women_dict.items()}
        
        encode = face_encode(img)
        
        proba_men = __men_model.predict_proba([encode[0]])
        proba_women = __women_model.predict_proba([encode[0]])
        
        probs_men = proba_men[0]
        probs_women = proba_women[0]
        result_men = []
        result_women = []
        
        # Track best match
        max_men_idx = int(np.argmax(probs_men))
        max_women_idx = int(np.argmax(probs_women))
        max_men_score = probs_men[max_men_idx]
        max_women_score = probs_women[max_women_idx]

        for idx, prob in enumerate(probs_men):
            result_men.append({label_dict_men[idx]: f'{round(prob*100, 2)}%'})
        for idx, prob in enumerate(probs_women):
            result_women.append({label_dict_women[idx]: f'{round(prob*100, 2)}%'})

        # Determine Best Match (Men or Women)
        best_category = 'Men' if max_men_score > max_women_score else 'Women'

        # Determine the actual best celebrity name
        best_match_name = (
            label_dict_men[max_men_idx]
            if best_category == 'Men'
            else label_dict_women[max_women_idx]
        )

        result = {
            'Men': result_men,
            'Women': result_women,
            'Best_Match': best_category,
            'Best_Celebrity': best_match_name
        }
        
        return result
        
    except Exception as e:
        raise Exception(f"Similarity error: {str(e)}")

def load_artifacts():
    global __men_dict, __men_model, __women_dict, __women_model
    
    try:
        with open('./artifacts/men_dict.json', 'r') as f:
            __men_dict = json.load(f)

        if __men_model is None:
            with open('./artifacts/men_face.pkl', 'rb') as f:
                __men_model = joblib.load(f)

        with open('./artifacts/women_dict.json', 'r') as f:
            __women_dict = json.load(f)

        if __women_model is None:
            with open('./artifacts/women_face.pkl', 'rb') as f:
                __women_model = joblib.load(f)

        print('Loading artifacts is done')
        
    except Exception as e:
        print(f"Error loading artifacts: {str(e)}")
        raise

if __name__ == "__main__":
    load_artifacts()
    print(classify_image(r'C:\Users\iamha\OneDrive\Documents\ImageClassification\Harshit_Image.jpg'))
    print(similarity(r'C:\Users\iamha\OneDrive\Documents\ImageClassification\Harshit_Image.jpg'))