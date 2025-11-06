🖼 Face Detection App (Streamlit + OpenCV)

This is a simple web application that detects human faces in uploaded images using OpenCV and Haar Cascade Classifier, built with Streamlit.


---

✅ Features

Upload any image (JPG/PNG)

Detect faces using Haar Cascade

Shows number of faces detected

Displays image with rectangles around detected faces



---

📁 Project Files
│
├── faceapp.py
├── FaceDetection.ipynb
├── haarcascade_frontalface_default.xml
├── teach.jpg
├── requirements.txt
├── README.md


---

⚙ Installation & Run

pip install streamlit opencv-python numpy
streamlit run app.py


---

🧠 How It Works

Image is uploaded using Streamlit

Converted to grayscale (required by OpenCV)

Faces are detected using detectMultiScale()

Boxes are drawn around detected faces and displayed



---

✅ Requirements

streamlit
opencv-python
numpy

---

🎥 Demo Video

You can watch the project in action here:

▶ [Click to watch Face.mp4](./Face.mp4)

Or download directly from this repository.

---


✅ Conclusion

This project demonstrates a simple and efficient face detection system using OpenCV and Streamlit. It successfully detects faces in images and provides a user-friendly interface. This serves as a good foundation for beginners and can be further improved with real-time webcam detection or advanced deep learning models.

---

👨‍💻 Author
👤 Kousik Chakraborty
📧 Email: www.kousik.c.in@gmail.com
🔗 GitHub Profile: https://github.com/iamkousikc-create18
🔗 Project Repository: https://github.com/iamkousikc-create18/Face-Detection
