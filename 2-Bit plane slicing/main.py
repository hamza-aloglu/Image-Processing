import numpy as np
import cv2

def int2bitarray(img):
    arr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
              for z in range(img.shape[2]):
                  arr.append(np.binary_repr(img[i][j][z], 8))
    return arr

imageCv = cv2.imread("eVcWGr6q_400x400.png")
arr = np.array(int2bitarray(imageCv))
arr = arr.reshape(imageCv.shape)

plane = np.zeros((imageCv.shape))
for k in range(0, 8):
      for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                  for z in range(arr.shape[2]):
                        plane[i, j, z] = int(arr[i, j, z][k])
      cv2.imwrite('./Bitplane' + str(7 - k) + '.png', plane * 255)
      print('\nbit plane ' + str(7 - k) + ' done!')


