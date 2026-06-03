import cv2

watch_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    objects = watch_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Object Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
