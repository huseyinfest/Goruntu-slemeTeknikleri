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

    # Görüntü üzerinde nesne tespiti yap (show=True KALDIRILDI)
    results = model(frame, conf=0.4) 

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

    # Sonuçları tek bir OpenCV penceresinde göster
    cv2.imshow('YOLO Detection', frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()