import cv2 as cv
import numpy as np
import pytesseract as pt




def processImage(img):

    #crop
    cropped = img[160:970, 1450:1850] #height then width
    cv.imshow('goblet cropped', cropped)

    #blank
    # blank = np.zeros(cropped.shape, dtype='uint8')
    # blank[:] = 255
    

    #grey
    # kernel = np.ones((5,5),np.float32)/25
    gray = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
    cv.imshow('goblet gray', gray)

    #blur
    # blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)
    # cv.imshow('goblet blur', blur)


    #threshold
    thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)[1]
    # thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #         cv.THRESH_BINARY,50,1)



    # double = cv.resize(thresh, None, fx=1.5, fy=1.5)
    cv.imshow('Thresh', thresh)

    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    # # Perform closing (dilation followed by erosion)
    # close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

    # invert
    invert = cv.bitwise_not(thresh)
    cv.imshow("goblet invert", invert)

  


    #contrast
    # contrast = 1.0001*invert 
    # alpha= 1.1
    # beta = 50
    # contrast = cv.convertScaleAbs(invert, alpha=alpha, beta=beta)
    # cv.imshow("goblet contrast", contrast)



    #gray to black
    # # Convert input RGB to HSV
    # hsv = cv.cvtColor(contrast, cv.COLOR_BGR2HSV)
    # # Get brightness channel
    # vChannel = hsv[:, :, 2]
    # bw = 255*np.uint8(vChannel < 200)  
    # cv.imshow("goblet gray to black", bw)

    

    #edge cascade
    # canny = cv.Canny(gray, 90, 450)
    # cv.imshow('goblet canny 90 450', canny)
    canny = cv.Canny(thresh, 90, 450)
    cv.imshow('goblet canny 90 450', canny)
    




    #contours onto blank
    # contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
    # print(f'{len(contours)} contours found!')
    # cv.drawContours(blank, contours, -1 , (0,0,0), thickness=1 )
    # cv.imshow('blank', blank)
    return canny


def readArtifact(imgFinal):
    storeline = ""
    txtList = []
    for i in pt.image_to_string(imgFinal):
        if i == "\n":
            txtList.append(storeline)
            storeline = ""
        storeline += i
    txtList.append(storeline)


    print(pt.image_to_string(imgFinal))
    print(txtList)
    return txtList


def processTxt(rawList):
    artifactTypes = ["Fl", "Fe", "Sa", "Go", "Ci"]
    for i in range(len(rawList)):
            if rawList[i] in artifactTypes:
                print("helloasdasfjoiuweojigewoij")
                break


            # any("ayy" in s for s in messageStore)






goblet = cv.imread('artifactsHydro/goblet.png')

artifactTxt = readArtifact(processImage(goblet))
processTxt(artifactTxt)



cv.waitKey(0)
# processImage(readArtifact(goblet = cv.imread(artifacts/goblet.jpg)))