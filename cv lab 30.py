import cv2

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)

    cv2.imshow("Smile Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
