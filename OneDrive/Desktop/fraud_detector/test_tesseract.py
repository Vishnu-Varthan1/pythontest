# test_tesseract.py
import pytesseract
from PIL import Image

# Point to your Tesseract exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Quick OCR test
img = Image.open("input/sample.jpg")   # put a test image here
text = pytesseract.image_to_string(img)
print("---- OCR RESULT ----")
print(text)
