# 🎬 Celebrity Image Classification & Similarity

A **Flask-based web application** that:

1. **Classifies** an uploaded celebrity image as **male or female**  
2. **Computes similarity** of the uploaded image against a dataset of Indian celebrities  
3. Displays **probability scores** and the **best matching celebrity** with confidence percentage  

---

## 📂 Project Structure

```
project/
├── dataset/                     # Original celebrity images (ignored in git)
├── server/
│   ├── server.py                # Flask backend
│   ├── util.py                  # Helper functions (face encoding, model loading)
│   ├── artifacts/               # Model and dictionary files (.pkl, .json)
│   ├── static/                  # JS, CSS, and other static files
│   ├── templates/               # HTML templates (app.html)
│   ├── Dockerfile               # Dockerfile for containerization
│   └── requirements.txt         # Python dependencies
├── Celebrity_Classifier.ipynb   # Notebook used for training/testing
├── Crawler.py                   # Script to collect dataset images
├── haar_eye.xml                 # Haarcascade for eyes
├── haar_face.xml                # Haarcascade for face
├── Procfile                     # For optional cloud hosting
└── README.md
```

---

## ⚡ Features

- **Image Upload & Preview** – Upload an image and preview it in the browser  
- **Celebrity Classification** – Classifies uploaded celebrity image as male or female  
- **Similarity Scoring** – Compares uploaded image against known celebrities and returns probability scores  
- **Best Match Highlight** – Displays the top-matching celebrity with confidence percentage  
- **Tailwind CSS UI** – Clean, responsive interface with automatic result display  

---

## 🚀 Run Locally

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
   cd server
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python server.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🐳 Run with Docker (Optional)

This project includes a **Dockerfile** for easy containerization.

1. **Build the Docker Image**
   ```bash
   cd server
   docker build -t celebrity-classification .
   ```

2. **Run the Container**
   ```bash
   docker run -p 5000:5000 celebrity-classification
   ```

Or pull the **prebuilt image** from Docker Hub:
```bash
docker pull iiamharshit237/imageclassification-similarity:latest
docker run -p 5000:5000 iiamharshit237/imageclassification-similarity
```

The app will be available at **http://localhost:5000**.

---

## 📜 License

This project is for **educational purposes**. You can modify and use it as needed.
