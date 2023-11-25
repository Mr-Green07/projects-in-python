from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("e:\my mobile photos and videos\IMG_20221024_191133.jpg")
plt.imshow(img1[:, :, ::-1])
plt.show