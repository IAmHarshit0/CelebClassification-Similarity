# 🎬 Celebrity Image Classification & Similarity

This project is a **Flask-based web application** that can:

1. **Classify** an uploaded image to identify whether the celebrity is male or female.  
2. **Compute similarity** of the uploaded image against a dataset of Indian celebrities and display the **probability scores** for each celebrity.  
3. Show the **best matching celebrity** and their confidence percentage.  

---

## 📂 Project Structure

```
project/
├── dataset/                 # Original celebrity images (ignored in git)
├── server/
│   ├── server.py            # Flask backend
│   ├── util.py              # Helper functions (face encoding, model loading)
│   ├── artifacts/           # Model and dictionary files (.pkl, .json)
│   ├── images/              # Small showcase images for UI
│   ├── static/              # JS, CSS, and other static files
│   └── templates/           # HTML templates (app.html)
├── Celebrity_Classifier.ipynb  # Notebook used for training/testing
├── Crawler.py               # Script to collect dataset images
├── haar_eye.xml             # Haarcascade for eyes
├── haar_face.xml            # Haarcascade for face
├── requirements.txt         # Python dependencies
├── Procfile                 # For Render deployment
├── package.json             # For Node-related UI (Tailwind)
└── .gitignore
```

---

## ⚡ Features

- **Image Upload & Preview** – Select an image.  
- **Celebrity Classification** – Determines if the celebrity is a man or woman.  
- **Similarity Scoring** – Compares uploaded image with dataset and gives probability scores.  
- **Best Match Highlight** – Displays the top-matching celebrity and category.  
- **Tailwind CSS UI** – Clean, responsive interface with automatic result display.  

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/celebrity-classification.git
   cd celebrity-classification
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   cd server
   python server.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📜 License

This project is for **educational purposes**. You can modify and use it as needed.

---