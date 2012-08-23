#####################################################
#  Copyright (c) 2012 Piyush Kant                   #
#  See the file license.txt for copying permission  #
#####################################################

import classifier
import math

class fisherclassifier(classifier.classifier):
    def __init__(self, getFeatures):
        classifier.classifier.__init__(self, getFeatures)
        self.minimum = {}
    
    #Pr(category|feature)
    def cProb(self, feat, cat):
        
        # The frequency of this feature in this category
        fp = self.featProb(feat, cat)
        if fp == 0: 
            return 0
        
        # The frequency of this feature in all the categories
        freqSum = sum([self.featProb(feat, c) for c in self.catList()])
        
        # The probability is the frequency in this category divided by the overall frequency
        p = fp / freqSum
        
        return p

    def fisherProb(self, item, cat):
        
        # Multiply all the probabilities together
        p = 1
        features = self.getFeatures(item)
        for feat in features:
            p *= (self.weightedProb(feat, cat, self.cProb))
        
        # Take the natural log and multiply by -2
        fscore = -2 * math.log(p)
        
        # Use the inverse chi2 function to get a probability
        return self.invchi2(fscore, len(features) * 2)
    
    def invchi2(self, chi, df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df // 2):
            term *= m / i
            sum += term
    
        return min(sum, 1.0)
    
    def setMinimum(self, cat, min):
        self.minimum[cat] = min
  
    def getMinimum(self, cat):
        if cat not in self.minimum: 
            return 0
        
        return self.minimum[cat]
    
    def classify(self, item, default=None):
    # Loop through looking for the best result
        best = default
        max = 0.0
        for c in self.catList():
            p = self.fisherProb(item, c)
            # Make sure it exceeds its minimum
            if p > self.getMinimum(c) and p > max:
                best = c
                max = p
    
        return best