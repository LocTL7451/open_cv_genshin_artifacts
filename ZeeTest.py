# Import required packages
import cv2
import pytesseract

#======================================
# Data Section
img_file = "cum.png"
output_file = "txt_output.txt"
#======================================

pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'
img = cv2.imread(img_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
processed_img = img.copy()
file = open(output_file, "w+")
file.write("")
file.close()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(processed_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = processed_img[y:y + h, x:x + w]
    file = open(output_file, "a")
    text = pytesseract.image_to_string(cropped)
    file.write(text)
    file.write("\n")
    file.close