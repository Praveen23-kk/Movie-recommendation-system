import cv2

# Load an image from file
image = cv2.imread("WhatsApp Image 2024-07-26 at 05.42.21_d487eb2f.jpg")

# Check if image is loaded properly
if image is None:
    print("Error: Image could not be loaded.")
    exit()

# Display the image in a window
cv2.imshow('Image', image)

# Wait for any key to close the window
cv2.waitKey(0)

# Save the image to a new file
cv2.imwrite('saved_image.jpg', image)

# Close all OpenCV windows
cv2.destroyAllWindows()
