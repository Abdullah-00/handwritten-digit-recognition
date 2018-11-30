"""
This program extracts digits from a scanned paged, in TIFF format, that contains handwritten Arabic numerals, where each
digit is written 15 times. The program extracts the digit as a TIFF image without any borders.

The extracted digits images will be used later to implement a an intelligent system that can automatically recognize
handwritten digits. This is part of Principles of Artificial Intelligence course's (ICS381) term project at KFUPM.

Note:
    To run this code, you need to install Pillow library

"""
from PIL import Image
import os

width, height = 147, 147 #The width and height of the cropped image containing the digit

x1_m1, y1_m1 = 530,504 #Coordinates of the top left corner of the top left cell of T1M1.tif
x1_m2, y1_m2 = 543,525 #Coordinates of the top left corner of the top left cell of T1M2.tif
x1_m3, y1_m3 = 547,530 #Coordinates of the top left corner of the top left cell of T1M3.tif

thickness = 19 #This is the distance between two cells

annotation_file_name = "Annotations_Tx.txt"



"""
x1, y1, x2, and y2 represents the coordinates of the rectangle that contains a digit

     width
       |
       |
       v
(x1,y1)-------
|             |
|             |
|    Digit    |  <--- height
|             |
|             |
 ----------(x2,y2)

"""




"""This function takes a folder containing the scanned pages as an input and pass each TIFF file to ExtractDigits(file).

Parameters:
    folder_loc (str): The folder containing the scanned pages images

"""
def ListScannedPages(folder_loc):

    os.makedirs("Digit Images")
    annotationCreator(annotation_file_name) # To create an annotation file list

    for sFile in os.listdir(folder_loc):
        fileName, fileExt = os.path.splitext(sFile)
        if fileExt == ".tif":
            if fileName == "T1M1":
                ExtractDigits(folder_loc + "/" + sFile, fileName, fileExt, x1_m1, y1_m1, width, height)
            elif fileName == "T1M2":
                ExtractDigits(folder_loc + "/" + sFile, fileName, fileExt, x1_m2, y1_m2, width, height)
            else:
                ExtractDigits(folder_loc + "/" + sFile, fileName, fileExt, x1_m3, y1_m3, width, height)





"""This function takes a location of a TIFF image as an input
 and extract/save each digit in that image as another TIFF image
 
 Parameters:
    file_loc (str): a location of a TIFF image containing Arabic numerals, where each number is repeated 14 times
    fileName (str): name of an image file 
    fileExt (str): extension of an image file (should be TIFF)
    x1, y1: Coordinates of the top left corner of the top left cell of the image 
"""
def ExtractDigits(file_loc, fileName, fileExt, x1, y1, width, height):
    image = Image.open(file_loc)

    if fileName == "T1M2":
        image = image.rotate(-0.49)
    elif fileName == "T1M3":
        image = image.rotate(-0.5)

    x2, y2 = x1 + width, y1 + height  # Coordinates of the bottom right corner of the top left cell

    digit = 0
    level = 15 # To start from the bottom of the image since the image is originally rotated
    while (digit <= 9):
        while (level > 0):
            imageName = fileName + "D-" + str(digit) + "_" + str(16-level) + fileExt #Name of the image file to be saved

            digit_image = image.crop((x1 + digit * (width+thickness), y1 + (level-1) * (width+thickness), x2 + digit * (width+thickness), y2 + (level-1) * (width+thickness))).rotate(-90)

            if imageName == "T1M2D-9_1.tif":# special case
                digit_image.paste("white", (0, 142, 147, 147))
            else:
                digit_image = whitenTheBorder(digit_image)  # To erase any border portions after cropping



            annotationFiller(imageName, str(digit), annotation_file_name) #Insert the file name and class to the annotation file list

            digit_image.save("Digit Images/" + imageName, dpi=(300,300))


            level -= 1
        digit += 1
        level = 15
    #print(file.filename, file.format, file.mode, file.info)



def whitenTheBorder(image):
    width = 10
    image.paste("white", (0, 0, 147, width))
    image.paste("white", (0, 0, width, 147))
    image.paste("white", (147-width, 0, 147, 147))
    image.paste("white", (0, 147-width, 147, 147))

    return image


"""This function create an empty annotation file with two columns, FileName and Class

 Parameters:
    fileName (str): the name of the annotation file to be created
"""
def annotationCreator(fileName):
    annoFile = open(fileName, "w+")
    annoFile.write("FileName \t \t Class\n")
    annoFile.close()





"""This function enters a new row to an existing annotation file

 Parameters:
    c1, c2 (str): to cells to be entered to a new row in an annotation file
    fileName (str): the location of an annotation file
"""
def annotationFiller(c1, c2, fileName):
    annoFile = open(fileName, "a+")
    row = c1 + " \t \t " + c2 + "\n"
    annoFile.write(row)
    annoFile.close()




def main():
    ListScannedPages("Scanned Pages")
    print("The above three red lines are not errors, these are just warnings. The program completed successfully")

main()


