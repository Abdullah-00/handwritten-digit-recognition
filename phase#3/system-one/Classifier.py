import math
from scipy import stats

class Classifier:
    def findProb(self, f, mean, stdev):
        prob = stats.norm(mean, stdev).pdf(f) + 1 / 60
        return prob

    def findProbPerClass(self, refrence, features):

        probs = {}

        for classValue in refrence:
            classRef = refrence[classValue]
            probs[classValue] = 0

            for i in range(len(classRef)):
                mean, stdev = classRef[i]
                f = features[i]

                probs[classValue] += math.log(self.findProb(f, mean, stdev))

        return probs

    def classify(self, refrence, features):
        probs = self.findProbPerClass(refrence, features)

        bestClass, bestProb = None, -9999

        for classVal, prob in probs.iteritems():
            if bestClass is None or prob > bestProb:
                bestProb = prob
                bestClass = classVal

        return bestClass, bestProb
