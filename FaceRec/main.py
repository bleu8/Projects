from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

img1="img1.jpg"
img2="imgg2.jpg"
resp=DeepFace.verify(img1,img2)

img1=cv2.imread("img1.jpg")
plt.imshow(img1)
plt.show()

img2=cv2.imread("imgg2.jpg")
plt.imshow(img2)
plt.show()




print(resp["verified"])

#resp parametreleri
"""{'verified': True,
 'distance': 0.1976265853817719,
 'max_threshold_to_verify': 0.4,
 'model': 'VGG-Face',
 'similarity_metric': 'cosine'}"""



#0.4< benzemez
#vgg face modeli
#%% Angelina Jolie-Jenifer Aniston
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt


img1="img1.jpg"
img3="img33.jpg" 
resp=DeepFace.verify(img1,img3)
 
print(resp["verified"])



#%%Facenet modeli---> Google

from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt


img1="img1.jpg"
img3="img33.jpg" 
resp=DeepFace.verify(img1,img3,model_name="Facenet")
 
print(resp["verified"])
