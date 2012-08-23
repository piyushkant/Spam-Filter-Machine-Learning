#####################################################
#  Copyright (c) 2012 Piyush Kant                   #
#  See the file license.txt for copying permission  #
#####################################################

import classifier

class naivebayes(classifier.classifier):
    def __init__(self, getFeatures):
        classifier.classifier.__init__(self, getFeatures)
        self.thresholds = {}
        
    # Pr(document|category)
    def docProb(self, item, cat):
        features = self.getFeatures(item)
        
        # Pr(document|category) = Pr(feature1|category)*Pr(feature2|category)...
        p = 1;
        for feat in features:
            p *= self.weightedProb(feat, cat, self.featProb)
        
        return p
    
    #prob = Pr(category|document) = Pr(document|category)*Pr(category)/Pr(document)
    def prob(self, item, cat):
        catProb = self.getCatCount(cat) / self.totalCatCount();
        documProb = self.docProb(item, cat)
        
        return documProb * catProb
    
    def setthreshold(self, cat, t):
        self.thresholds[cat] = t
    
    def getthreshold(self, cat):
        if cat not in self.thresholds: 
            return 1.0
        
        return self.thresholds[cat]
    
    def classify(self, item, default=None):
        probs = {}
        
        # Find the category with the highest probability
        max = 0.0
        for cat in self.catList():
            probs[cat] = self.prob(item, cat)
            if probs[cat] > max:
                max = probs[cat]
                best = cat
                
        # Make sure the probability exceeds threshold*next best
        for cat in probs:
            if cat == best: 
                continue
            if probs[cat] * self.getthreshold(best) > probs[best]: 
                return default
        
        return best
