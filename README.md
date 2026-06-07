# 🎨 AI-Powered Image Colorization
---
## 🚀 Project Overview

Image Colorization is a Deep Learning-based web application that automatically converts grayscale (black & white) images into realistic color images.

Using a pre-trained Convolutional Neural Network (CNN), the model predicts color information for each pixel and generates visually appealing colorized outputs.

This project combines **Computer Vision**, **Deep Learning**, and **Web Development** to create an interactive and user-friendly image colorization platform.

---

## ✨ Key Features

✅ Upload black & white images instantly

✅ AI-powered automatic colorization

✅ Modern drag-and-drop interface

✅ Real-time image processing

✅ Download colorized images

✅ Responsive and attractive UI

✅ Fast and lightweight deployment

---

## 🖼️ Application Workflow

```text
Upload Image
      ↓
Image Preprocessing
      ↓
Deep Learning Model
      ↓
Color Prediction
      ↓
Generate Colorized Image
      ↓
Display & Download Result
```

---

## 🧠 Deep Learning Model

This project uses OpenCV's pre-trained Image Colorization model based on the Caffe framework.

### Model Files


* colorization_deploy_v2.prototxt
* colorization_release_v2.caffemodel https://1drv.ms/u/c/66d57ea21998d120/IQB2T75G1lgyT7n_LC3ZBSLTAW4BIebTEsWcsaVQYuh8a5k?e=roXajE
* pts_in_hull.npy


The model has been trained on millions of color images and learns to predict realistic color distributions from grayscale inputs.

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask
* Python

### Deep Learning & Computer Vision

* OpenCV
* NumPy
* Caffe Pretrained Model

---

## 📂 Project Structure

```text
ImageColorization/
│
├── app.py
├── colorization_deploy_v2.prototxt
├── colorization_release_v2.caffemodel 
├── pts_in_hull.npy
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── outputs/
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ImageColorization.git
cd ImageColorization
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install flask opencv-python numpy
```

---

## ▶️ Run Locally

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📸 Sample Results

| Original Image      | Colorized Output         |
| ------------------- | ------------------------ |
|<img width="183" height="275" alt="download (1)" src="https://github.com/user-attachments/assets/09e85c65-0404-4da6-8169-9180c38672fc" /> |<img width="183" height="275" alt="result" src="https://github.com/user-attachments/assets/1881408c-3922-4f68-922d-d9656f547661" /> |


---

## 🎯 Skills Demonstrated

* Deep Learning
* Computer Vision
* Image Processing
* Flask Development
* OpenCV DNN Module
* Frontend Design
* Model Integration
* Git & GitHub

---

## 🔮 Future Enhancements

* 🎥 Video Colorization
* 📱 Mobile-Friendly Interface
* ☁️ Cloud Deployment
* 📂 Batch Image Processing
* 🖼️ Before/After Comparison Slider
* 🤖 Advanced GAN-based Colorization

---

## 👩‍💻 Author

### Samruddhi Shivtare


