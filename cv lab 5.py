import cv2
import matplotlib.pyplot as plt

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print(" Error loading image")
else:
    colors = ('b','g','r')

    for i, col in enumerate(colors):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist, color=col)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()
