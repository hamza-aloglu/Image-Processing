import cv2
import numpy as np


def contraharmonic_mean_filter(image, window_size, Q):
    padded_image = cv2.copyMakeBorder(image, window_size // 2, window_size // 2, window_size // 2, window_size // 2,
                                      cv2.BORDER_CONSTANT)
    filtered_image = np.zeros_like(image, dtype=np.float32)

    for i in range(window_size // 2, padded_image.shape[0] - window_size // 2):
        for j in range(window_size // 2, padded_image.shape[1] - window_size // 2):
            window = padded_image[i - window_size // 2:i + window_size // 2 + 1,
                     j - window_size // 2:j + window_size // 2 + 1]
            numerator = np.sum(np.power(window, Q + 1))
            denominator = np.sum(np.power(window, Q))

            if denominator != 0:
                filtered_image[i - window_size // 2, j - window_size // 2] = numerator / denominator

    return np.uint8(np.clip(filtered_image, 0, 255))


# Load the image
image = cv2.imread('kolala.png', cv2.IMREAD_GRAYSCALE)

# Set the window size and Q value
window_size = 3
Q = 1.5

# Apply the contraharmonic mean filter
filtered_image = contraharmonic_mean_filter(image, window_size, Q)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Contraharmonic Mean Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
