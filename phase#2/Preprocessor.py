from PIL import Image, ImageFilter
import os
import numpy as np

trainSetSize = 1800
devSetSize = 900
threshold = 252
nSize = 35
def ProcessImages(folder_loc, setType):
    folderName = setType + "_processed"
    if os.path.exists(folderName):
        os.system("rm -rf " + folderName)   # To remove the dir if it already exists
    os.makedirs(folderName)

    for sFile in os.listdir(folder_loc):
        print "Pre-processing: " + sFile
        fileName = os.path.basename(sFile)
        imagePath = folder_loc + "/" + sFile
        image = Image.open(imagePath)

        image = convertToGreyScale(image)

        image = removeSaltAndPepper(image.convert("L"), sFile)

        # image = convertToBlackAndWhite(image)
        # imageName = "baw-" + fileName
        # image.save("no-pepper-no-salt/" + imageName, dpi=(300, 300))

        if sFile is "train587.tif" or "train97.tif":  # Excepted because of their poor quality
            image = removeBackgroundAndBorders(image.convert("L"), 253)
        else:
            image = removeBackgroundAndBorders(image.convert("L"), threshold)

        image.save(folderName + "/" + sFile)


def removeBackgroundAndBorders(image, threshold):
    width, height = image.size
    imageArr = np.asmatrix(image.convert("L"))

    newArr = []  # it will contain the image array after removing the background
    newSize = 0  # the new size after removing the background


    for row in imageArr:
        innerRow = np.asarray(row[0])
        rowContent = innerRow[0]
        if sum(rowContent) < width * threshold:
            newSize = newSize + 1
            newArr.append(innerRow)

    newImageArr = np.reshape(newArr, (newSize, width))   # the image array after removing horizontal background
    image = Image.fromarray(newImageArr)  # convert the array back to an image

    height, width = image.size  # height and width are swapped because the image is going to be transposed

    imageArr = np.asmatrix(image.convert("L"))
    imageArr = imageArr.transpose()  # Exchange rows with columns

    newArr = []  # it will contain the image array after removing the background
    newSize = 0  # the new size after removing the background

    for row in imageArr:
        innerRow = np.asarray(row[0])
        rowContent = innerRow[0]
        if sum(rowContent) < width * threshold:
            newSize = newSize + 1
            newArr.append(innerRow)

    newImageArr = np.reshape(newArr, (newSize, width))   # the image array after removing vertical background
    newImageArr = imageArr.transpose()  # Exchange rows with columns (back to normal)

    image = Image.fromarray(newImageArr)  # convert the array back to an image
    image = image.resize((nSize, nSize), Image.ANTIALIAS)   # normalize the image to the new size

    return image



def convertToBlackAndWhite(image):
    image = image.convert("1")  # convert the image to black and white
    return image

def convertToGreyScale(image):
    image = image.convert("L")  # convert the image to black and white
    return image

def removeSaltAndPepper(image, fileName):
    if fileName is "train587.tif" or "train97.tif":   # Excepted because of their poor quality
        image = image.filter(ImageFilter.MedianFilter(1))
    else:
        image = image.filter(ImageFilter.MedianFilter(3))
    return image

if __name__ == '__main__':
    # print "Start pre-processing the train set"
    # ProcessImages("annotations/train", "Train_set")
    # print "End of pre-processing the train set"
    # print "Start pre-processing the dev set"
    # ProcessImages("annotations/dev", "Dev_set")
    # print "End of pre-processing the dev set"
    # print "The above red lines are not errors, these are just warnings."
    # print "The program completed successfully"

    threshold = 252
    nsize = 35
    if True:
        for o in range(1, trainSetSize + 1):
            filename = "train%d.tif" % o
            image = Image.open("annotations/train/" + filename)
            image = image.convert("L")

            if filename is "train587.tif" or "train97.tif":  # Excepted for their bad quality
                image = image.filter(ImageFilter.MedianFilter(1))
                threshold = 253
            else:
                image = image.filter(ImageFilter.MedianFilter(3))

            width, height = image.size
            arr = np.asmatrix(image)

            emptyArr = []
            height = 0
            for row in arr:
                row = np.asarray(row[0])
                myRow = row[0]
                if sum(myRow) < threshold * width:
                    height = height + 1
                    emptyArr.append(row)

            ar = np.reshape(emptyArr, (height, width))
            print filename
            newImage = Image.fromarray(ar, None)
            image = newImage
            height, width = image.size

            arr = np.asmatrix(image.convert("L"))
            arr = arr.transpose()

            emptyArr = []
            height = 0
            for row in arr:
                row = np.asarray(row[0])
                myRow = row[0]
                if sum(myRow) < threshold * width:
                    height = height + 1
                    emptyArr.append(row)

            ar = np.reshape(emptyArr, (height, width))
            ar = ar.transpose()
            newImage = Image.fromarray(ar, None)
            newImage = newImage.resize((nsize, nsize), Image.ANTIALIAS)

            newImage.save("Train_set_processed/" + filename)
        print "Train set finished"

    if True:
        for o in range(1, devSetSize + 1):
            # filter out rows
            filename = "dev%d.tif" % o
            image = Image.open("annotations/dev/" + filename)
            image = image.convert("L")
            image = image.filter(ImageFilter.MedianFilter(3))
            width, height = image.size
            arr = np.asmatrix(image)
            emptyArr = []
            height = 0
            for row in arr:
                row = np.asarray(row[0])
                myRow = row[0]
                if sum(myRow) < threshold * width:
                    height = height + 1
                    emptyArr.append(row)
            ar = np.reshape(emptyArr, (height, width))
            print filename
            newImage = Image.fromarray(ar, None)
            image = newImage
            height, width = image.size
            arr = np.asmatrix(image.convert("L"))
            arr = arr.transpose()
            emptyArr = []
            height = 0
            for row in arr:
                row = np.asarray(row[0])
                myRow = row[0]
                if sum(myRow) < threshold * width:
                    height = height + 1
                    emptyArr.append(row)
            ar = np.reshape(emptyArr, (height, width))
            ar = ar.transpose()
            newImage = Image.fromarray(ar, None)
            newImage = newImage.resize((nsize, nsize), Image.ANTIALIAS)
            newImage.save("Dev_set_processed/" + filename)
        print "Dev set finished"

