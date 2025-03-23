# YOLOv11 Object Detection Web App (Django)

This is a Django-based web application that allows users to upload images and detect objects using a trained YOLOv11 model.

## 🚀 Features

- Upload images through a web interface
- Perform object detection using a YOLOv11 model (`best.pt`)
- Display detected objects with bounding boxes
- Show object names and confidence scores
- Attractive frontend with Bootstrap

---

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

## 📌 Usage

1. **Upload an Image**: Select an image and click `Detect Objects`.
2. **Detection Process**: The model processes the image and identifies objects.
3. **Results Display**: The detected objects, bounding boxes, and confidence scores appear on the webpage.

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

## 📜 License

This project is open-source and available under the MIT License.

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! 😃

**Developed by [Your Name]** 🚀

