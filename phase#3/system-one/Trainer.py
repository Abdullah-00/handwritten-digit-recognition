from PIL import Image
import numpy as np


class Trainer:

    def __init__(self, extractor, classifier):
        self.extractor = extractor
        self.classifier = classifier

    def openAnnoFile(self, fileName):
        Ref = {}
        refFile = open(fileName)

        words = refFile.read()

        lines = words.split('\n')

        for line in lines:
            lineArr = line.split('	')
            if len(lineArr) <= 1:
                break

            imgName, digClass = lineArr
            Ref[imgName] = digClass

        return Ref

    def featuresResultContainer(self):
        featuresCont = {}

        for x in xrange(10):
            featuresCont[x] = [[] for i in range(self.extractor.totalFeatures())]    # to contain the feature for each digit

        return featuresCont

    def train(self, trainRef, featuresCont, filename):
        digClass = trainRef[filename]
        digClass = int(digClass)

        image = Image.open("Train_set_processed/" + filename)

        imageArr = np.asarray(image.convert("L"))

        feature = featuresCont.get(digClass)

        for index, featureValue in enumerate(self.extractor.extractFeatures(imageArr)):
            feature[index].append(featureValue)

        featuresCont[digClass] = feature

    def executeOnDev(self, ref, fileName):
        image = Image.open("Dev_set_processed/" + fileName)

        imageArr = np.asarray(image.convert("L"))

        features = self.extractor.extractFeatures(imageArr)

        return self.classifier.classify(ref, features)

    def executeOnTest(self, ref, fileName):
        image = Image.open("Test_set_processed/" + fileName)

        imageArr = np.asarray(image.convert("L"))

        features = self.extractor.extractFeatures(imageArr)

        return self.classifier.classify(ref, features)

    def record(self, AnnoFile):
        record = {}
        for digClass in range(0, 10):
            dig = []
            features = AnnoFile.get(digClass)

            for feature in features:
                mean = np.mean(feature)
                std = np.std(feature)
                dig.append((mean, std))

            record[digClass] = dig

        return record
