import cv2
import streamlit as st
import numpy as np   #helps convert image format
from PIL import Image  #read upload images

st.title("Face Detection App")

#upload an image
upload_file=st.file_uploader("Upload an Image",["jpg","png","jpeg"])
face_cap=cv2.CascadeClassifier(r"C:\Users\USER\Desktop\HaarCascade\haarcascade_frontalface_default.xml")

if upload_file:
    img=np.array(Image.open(upload_file))  #convert the uploaded image into numpy array.OPENCV can only process numpy array.
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Face detection works Better on grayscale images
    faces=face_cap.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    st.image(img,channels="RGB",caption=f"Detected {len(faces)} faces")  #Shows how many faces are detected
else:
    st.info("Upload an image to start detection") #Shows an instruction message when no file is uploaded