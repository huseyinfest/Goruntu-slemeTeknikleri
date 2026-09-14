import cv2 as cv
import numpy as np

# Görseli yerel diskten RAM'e yükle
#img = cv2.imread('ornek_gorsel.jpg')

# Resmi bir pencerede göster
#cv2.imshow('Gorsel Analizi', img)

# Kullanıcı herhangi bir tuşa basana kadar pencereyi açık tut (0 = sonsuz)
#cv2.waitKey(0)

# Açık olan tüm GUI pencerelerini kapat ve belleği serbest bırak
#cv2.destroyAllWindows()

# BGR formatından Grayscale formata dönüştür
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# (5, 5) çekirdek boyutu (kernel) filtre şiddetini belirler. Tek sayı olmalıdır.
#blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Alt eşik: 50, Üst eşik: 150
#edges = cv2.Canny(blurred_img, 50, 150)

# OpenCV'nin sistemdeki varsayılan yüz modelini yükle
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Yüzlerin koordinatlarını bul
# scaleFactor: Kamera yakınlığını tolere eder, minNeighbors: Yanlış pozitifleri eler
#faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# Bulunan yüzlerin (x,y) koordinatlarına dikdörtgen (bounding box) çiz
#for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
#cv2.imshow('Tespit Edilen Yuzler', img)
#cv2.waitKey(0)
