"""
Team#1 contribution:
Mohammed Alswailem		201336010:  33.33%
Ahmed Algarni			201453160:  33.33%
Abdullah Alshoshan		201442960:  33.33%
"""

from Trainer import Trainer
from FeatureExt import Extractor
from Classifier import Classifier


trainSetSize = 1800
devSetSize = 900

if __name__ == '__main__':



    ext = Extractor()

    trainer = Trainer(ext, Classifier())

    trainAnno = trainer.openAnnoFile("annotations/train.txt")
    container = trainer.featuresResultContainer()

    ############################################

    print "Training started"

    for n in range(1, trainSetSize+1):
        filename = "train%d.tif" % n
        print filename
        trainer.train(trainAnno, container, filename)

    trainRef = trainer.record(container)

    ###############################################

    print "Dev set recognition started"

    devRef = trainer.openAnnoFile("annotations/dev.txt")


    rightNum = 0.0
    percentage = 0.0

    for n in range(1, devSetSize+1):
        filename = "dev%d.tif" % n
        print filename
        predClass, probability = trainer.execute(trainRef, filename)

        actualClass = int(devRef[filename])
        if actualClass == int(predClass):
            rightNum += 1
    percentage = (rightNum / (devSetSize+1)) * 100
    print "*** Recognition Result : ", str(percentage) + "% ***"

