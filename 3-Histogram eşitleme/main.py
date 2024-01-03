import cv2
import numpy as np

def convertGray(image):
    # Convert the image to grayscale using cv2.cvtColor
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def getHistogram(image):
    resultArray = np.zeros(256)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            resultArray[image[i, j]] += 1
    return resultArray

def syncHistogram(histogramArray, imageSize, L):
    newValues = np.zeros(len(histogramArray))
    newValues[0] = histogramArray[0]
    for i in range(1, len(newValues)):
        newValues[i] = int(histogramArray[i]) + int(newValues[i - 1])
    for i in range(newValues.shape[0]):
        newValues[i] = round(((newValues[i] - min(histogramArray)) / (imageSize - min(histogramArray))) * (2**L - 1))
    return newValues

def syncImageHistogram(image, newValues):
    resultImage = np.zeros((image.shape[0], image.shape[1], 1), dtype=np.uint8)
    for i in range(resultImage.shape[0]):
        for j in range(resultImage.shape[1]):
            resultImage[i, j] = newValues[image[i, j]]
    return resultImage

image = cv2.imread('nature.png')
image = convertGray(image)
histogramArray = getHistogram(image)

newValues = syncHistogram(histogramArray, image.shape[0] * image.shape[1], 8)
hstImage = syncImageHistogram(image, newValues)
cv2.imshow("Histogram Image", hstImage)
cv2.waitKey(0)
