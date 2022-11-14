import cv2 as cv
import numpy as np
import pytesseract as pt




def processImage(img):
    #crop
    cropped = img[160:970, 1450:1850] #height then width
    cv.imshow('feather cropped', cropped)

    #grey
    gray = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
    cv.imshow('feather gray', gray)

    #edge cascade
    # canny = cv.Canny(gray, 150, 450)
    # cv.imshow('feather canny 100 460', canny)
    canny = cv.Canny(gray, 150, 450)
    cv.imshow('feather canny 100 450', canny)
    
    #contours
    # contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
    # print(f'{len(contours)} contours found!')

    return canny


def readArtifact(imgFinal):
    # for i in range(len(pt.image_to_string(imgFinal))):
    #     txtList.append(i)

    print(pt.image_to_string(imgFinal))
    
    pass

feather = cv.imread('artifacts/feather.png')

readArtifact(processImage(feather))




cv.waitKey(0)
# processImage(readArtifact(feather = cv.imread(artifacts/feather.jpg)))