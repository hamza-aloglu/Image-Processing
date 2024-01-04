from PIL import Image
import numpy as np


def segment_image(image_path, threshold):
    # Resmi yükle
    img = Image.open(image_path)

    # NumPy dizisine dönüştür
    img_array = np.array(img)

    # Resmi RGB renk uzayına dönüştür
    if img_array.shape[2] == 4:  # Eğer resim RGBA formatındaysa
        img_array = img_array[:, :, :3]  # Alpha kanalını kaldır

    # Resmi bölütleyin
    segmented_image = np.zeros_like(img_array)
    segmented_image[img_array > threshold] = 255  # Eşik değerinden büyük pikselleri beyaz yap

    # Sonucu görüntüle
    segmented_img = Image.fromarray(segmented_image.astype('uint8'))
    segmented_img.show()


# Örnek kullanım
image_path = './kolala.png'
threshold_value = 128  # Eşik değeri, isteğe bağlı olarak ayarlayabilirsiniz
segment_image(image_path, threshold_value)
