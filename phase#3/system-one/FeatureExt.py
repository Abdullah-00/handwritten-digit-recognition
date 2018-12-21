
threshold = 239

def verticalAvgUp(img):
    h = len(img)
    w = len(img[0])

    contours = []

    for i in range(w):
        blackPixLocation = -9999

        for j in range(h):
            pix = img[j, i]

            if threshold >= pix:
                blackPixLocation = j

        if blackPixLocation != -9999:
            contours.append(h - blackPixLocation)

    summ = sum(contours) + 1
    count = len(contours) + 1

    return summ / count


def horizontalAvgUp(img):
    img = img.transpose()

    h = len(img)
    w = len(img[0])

    contours = []

    for i in range(w):
        blackPixLocation = -9999

        for j in range(h):
            pix = img[j, i]

            if threshold >= pix:
                blackPixLocation = j

        if blackPixLocation != -9999:
            contours.append(h - blackPixLocation)

    summ = sum(contours) + 1
    count = len(contours) + 1

    return summ / count


def verticalAvgLow(img):
    h = len(img)
    w = len(img[0])

    contours = []

    for i in range(w):
        blackPixLocation = -9999

        for j in range(h):
            pix = img[j, i]

            if threshold >= pix:
                blackPixLocation = j
                break

        if blackPixLocation != -9999:
            contours.append(h - blackPixLocation)

    summ = sum(contours) + 1
    count = len(contours) + 1

    return summ / count


def horizontalAvgLow(img):
    img = img.transpose()

    h = len(img)
    w = len(img[0])

    contours = []

    for i in range(w):
        blackPixLocation = -9999

        for j in range(h):
            pix = img[j, i]

            if threshold >= pix:
                blackPixLocation = j
                break

        if blackPixLocation != -9999:
            contours.append(h - blackPixLocation)

    summ = sum(contours) + 1
    count = len(contours) + 1

    return summ / count


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


class Extractor:

    def extractors(self):
        return [verticalAvgUp, horizontalAvgUp, verticalAvgLow, horizontalAvgLow, countBlackVertical, countBlackHorizontal]

    def extractFeatures(self, img):
        return [f(img) for f in self.extractors()]

    def totalFeatures(self):
        return len(self.extractors())
