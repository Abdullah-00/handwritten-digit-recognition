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

width, height = 147, 153 #The width and height of the cropped image containing the digit
x1, y1 = 529,502 #Coordinates of the top left corner of the top left cell
x2, y2 = x1 + width, y1 + height #Coordinates of the bottom right corner of the top left cell

thickness = 19 #This is the distance between a two cells
digit = 9
level = 14


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




"""This method takes a folder containing the scanned pages as an input and pass each TIFF file to ExtractDigit(file).

Parameters:
    folder_loc (str): The folder containing the scanned pages images

"""
def ListScannedPages(folder_loc):

    for sFile in os.listdir(folder_loc):
        fileName, fileExt = os.path.splitext(sFile)




