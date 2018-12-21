
threshold = 239


class Extractor:

    def extractors(self):
        return [blackWhiteTransition1, avgBlock1, avgBlock2, avgBlock3, avgBlock4, centerDistW, centerDistH, pixelByPixel, countBlackVertical, countBlackHorizontal]


    def extractFeatures(self, img):
        return [f(img) for f in self.extractors()]

    def totalFeatures(self):
        return len(self.extractors())

def pixelByPixel(img):
    h = len(img)
    w = len(img[0])

    contours = []

    for i in range(w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix:
                contours.append(1.0)
            else:
                contours.append(0.0)

    return sum(contours)

def blackWhiteTransition1(img):
    h = len(img)
    w = len(img[0])

    count = 0

    if(img[1,1] <= threshold):
        check = True #Balck
    else:
        check = False #White

    for i in range(w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix and not check:
                count += 1
                check = True
            elif threshold<= pix and check:
                count += 1
                check = False

    return count

def centerDistW(img):
    h = len(img)
    w = len(img[0])

    centerW = int(w/2.0)
    centerH = int(h/2.0)

    distW = 0
    distH = 0

    for i in range(w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix:
                distH += j-centerH
                distW += i-centerW

    return distW

def centerDistH(img):
    h = len(img)
    w = len(img[0])

    centerW = int(w/2.0)
    centerH = int(h/2.0)

    distW = 0
    distH = 0

    for i in range(w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix:
                distH += j-centerH
                distW += i-centerW

    return distH

# def avgBlock1(img):
#     h = len(img)
#     w = len(img[0])
#
#     propW = 0
#     propH = 0
#
#     lst =[]
#
#     for i in range(1, 4):
#         prevPropW = propW
#         prevProbH = propH
#         propW = i*w/3
#         propH = i*h/3
#
#         count = 0
#
#         for z in range(prevPropW, propW):
#             for j in range(prevProbH, propH):
#                 pix = img[j, z]
#                 if threshold >= pix:
#                     count += 1
#         lst.append(count)
#
#     summ = sum(lst)
#     return summ/len(lst)

def avgBlock1(img):
    h = len(img)/2
    w = len(img[0])/2
    count = 0
    for i in range(w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix:
                count += 1

    return count


def avgBlock2(img):
    h = len(img) / 2
    w = 2*len(img[0]) / 2
    count = 0
    for i in range(len(img[0]) / 2, w):
        for j in range(h):
            pix = img[j, i]
            if threshold >= pix:
                count += 1

    return count

def avgBlock3(img):
    h = 2*len(img) / 2
    w = len(img[0]) / 2
    count = 0
    for i in range(w):
        for j in range(len(img) / 2, h):
            pix = img[j, i]
            if threshold >= pix:
                count += 1

    return count

def avgBlock4(img):
    h = 2*len(img) / 2
    w = 2*len(img[0]) / 2
    count = 0
    for i in range(len(img[0]) / 2, w):
        for j in range(len(img) / 2, h):
            pix = img[j, i]
            if threshold >= pix:
                count += 1

    return count

def countBlackVertical(img):
    count = 1

    for row in img:
        isBlack = False

        for pix in row:
            if threshold >= pix and isBlack is False:
                isBlack = True
                count += 1

            if threshold <= pix:
                isBlack = False

    return count

def countBlackHorizontal(img):
    img = img.transpose()

    count = 1

    for row in img:
        isBlack = False

        for pix in row:
            if threshold >= pix and isBlack is False:
                isBlack = True
                count += 1

            if threshold <= pix:
                isBlack = False

    return count

# def blackWhiteTransition2(img):
#     h = len(img)
#     w = len(img[0])
#
#     count = 0
#
#     if(img[1,1] <= threshold):
#         check = True #Balck
#     else:
#         check = False #White
#
#     for i in range(h):
#         for j in range(w):
#             pix = img[j, i]
#             if threshold >= pix and not check:
#                 count += 1
#                 check = True
#             elif threshold<= pix and check:
#                 count += 1
#                 check = False
#
#     return count
