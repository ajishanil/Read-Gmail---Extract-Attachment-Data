"""
Packages for this file:

1.pytesseract
    -OCR engine to convert image to text
    -also important to install the tesseract ocr engine
        -> brew install tesseract / pip install tesseract
"""
import pytesseract
import os


# function to convert images to text
def convertImages(inputImageFolder, outputTextFolder):
    for file in os.listdir(inputImageFolder):
        # Splitting file name and extension
        fileName = file.split('.')[0]
        fileExtension = file.split('.')[1]

        # Full paths of files
        absImageFilePath = os.path.join(inputImageFolder, file)
        absTextFilePath = os.path.join(outputTextFolder, fileName + '.txt')

        # Valid extension list for pytesseract ocr
        validExtension = ['png', 'jpg', 'jpeg']

        # Converting image to text
        try:
            if fileExtension in validExtension:
                imageToText(absImageFilePath, absTextFilePath)

        except FileNotFoundError:
            print("File not supported")


# Function to convert an image to text
def imageToText(inImgage, outText):
    outputStr = pytesseract.image_to_string(inImgage)
    with open(outText, 'w') as f:
        f.write(outputStr)
