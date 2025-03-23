import torch
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from ultralytics import YOLO
import cv2
import numpy as np
import os

# Load YOLOv11 model
model = YOLO("yolo_app/models/best.pt")

def detect_objects(image_path):
    results = model(image_path)

    # Load image
    image = cv2.imread(image_path)

    # Process results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            label = f"{result.names[box.cls[0].item()]}: {conf:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save detected image
    output_path = os.path.join("media", "detections", os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    return output_path

def index(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            image_path = image_instance.image.path

            # Perform YOLOv11 object detection
            detected_image_path = detect_objects(image_path)

            return render(request, "index.html", {
                "form": form,
                "uploaded_image": image_instance.image.url,
                "detected_image": f"/media/detections/{os.path.basename(detected_image_path)}"
            })
    else:
        form = ImageUploadForm()

    return render(request, "index.html", {"form": form})
