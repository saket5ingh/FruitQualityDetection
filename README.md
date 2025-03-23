# YOLOv11 Fruit Quality Detection

This repository contains a complete Django web application for  fruit qualitydetection using YOLOv11 models. The application allows users to upload images, processes them with a pre-trained YOLOv11 model, and displays the detection results.

## Features

- User-friendly web interface for image upload
- Integration with YOLOv11 object detection model
- Real-time image preview before submission
- Display of original and processed images side-by-side
- Responsive design using Bootstrap

## Prerequisites

- Python 3.8+
- Django 4.0+
- PyTorch 1.12+
- OpenCV
- A trained YOLOv11 model file (best.pt)

## 📂 Project Structure

```
.
├── yolo_app/
│   ├── models/
│   │   ├── best.pt  # Your trained YOLOv11 model
│   ├── static/
│   │   ├── css/  # Frontend styles
│   │   ├── js/   # Scripts (if any)
│   ├── templates/
│   │   ├── index.html  # Web UI
│   ├── views.py  # Main backend logic
├── media/
│   ├── uploads/  # Uploaded images
│   ├── detections/  # Processed images with detected objects
├── manage.py
└── README.md
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download YOLOv11 Model (`best.pt`)

Place your trained `best.pt` model inside the `yolo_app/models/` directory.

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Django Server

```bash
python manage.py runserver
```

Now, open `http://127.0.0.1:8000/` in your browser. 🎯

---

## Usage

1. Access the web application at `http://127.0.0.1:8000`
2. Upload an image using the provided form
3. Click the "Detect Objects" button
4. View the detection results on the next page
5. Use the "Upload Another Image" button to process more images
---

## 🐞 Troubleshooting

### Image Upload Not Working?

- Check if `media/uploads/` and `media/detections/` exist.
- Ensure `MEDIA_URL` and `MEDIA_ROOT` are correctly set in `settings.py`.
- Restart the server after making changes.

### No Objects Detected?

- Ensure `best.pt` is trained properly.
- Try a different image.

---
## 🤝 Contributing

Pull requests and feature suggestions are welcome! 😃

