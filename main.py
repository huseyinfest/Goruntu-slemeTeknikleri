<<<<<<< HEAD
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
=======
import cv2
#import serial
import time
from ultralytics import YOLO

# Modeli yükle
model = YOLO('yolo11n.pt')

# Arduino'ya bağlan
#arduino = serial.Serial('COM3', 9600)  # Port numarasını sistemine göre ayarla
#time.sleep(2)  # Bağlantı kurulmasını bekle

# Video kaynağını ayarla (0, webcam için)
cap = cv2.VideoCapture(0)

# Veri gönderim döngüsü
while True:
    ret, frame = cap.read()  # Webcam'den bir kare oku
    if not ret:
        break  # Eğer kare okunamazsa döngüyü kır

    # Görüntü üzerinde nesne tespiti yap
    results = model(frame, show=True, conf=0.4)  # Tespitleri göster

    # Tespit edilen nesneleri döngüyle işle
    for result in results:
        for detection in result.boxes.data:  # Her bir tespit için
            # Tespit edilen nesnenin adı ve güven oranını al
            class_id = int(detection[5])  # Nesne sınıfı
            confidence = float(detection[4])  # Güven oranı

            # Sınıf ID'sini kullanarak nesne adını belirle
            object_name = model.names[class_id] if class_id < len(model.names) else "Bilinmeyen"

            # LCD ekranı güncellemek için nesne adını gönder
#            arduino.write((object_name + '\n').encode())  # Arduino'ya nesne adını gönder
#            print(f"Veri gönderildi: {object_name}")  # Konsola yaz

            # Tespit edilen nesnenin etrafına dikdörtgen çiz
            x1, y1, x2, y2 = map(int, detection[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{object_name} ({confidence:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow('YOLO Detection', frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break  # Eğer kare okunamazsa döngüyü kır

    # Görüntü üzerinde nesne tespiti yap
    results = model(frame, show=True, conf=0.4)  # Tespitleri göster

    # Tespit edilen nesneleri döngüyle işle
    for result in results:
        for detection in result.boxes.data:  # Her bir tespit için
            # Tespit edilen nesnenin adı ve güven oranını al
            class_id = int(detection[5])  # Nesne sınıfı
            confidence = float(detection[4])  # Güven oranı

            # Sınıf ID'sini kullanarak nesne adını belirle
            object_name = model.names[class_id] if class_id < len(model.names) else "Bilinmeyen"

            # LCD ekranı güncellemek için nesne adını gönder
#            arduino.write((object_name + '\n').encode())  # Arduino'ya nesne adını gönder
#            print(f"Veri gönderildi: {object_name}")  # Konsola yaz

#    time.sleep(1)  # Tespit aralığı (1 saniye)

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
>>>>>>> 06c373e086f24263162db712b7566505ed5ebe5b
