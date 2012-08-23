#####################################################
#  Copyright (c) 2012 Piyush Kant                   #
#  See the file license.txt for copying permission  #
#####################################################

class classifier:
    def __init__(self, getFeatures, filename=None):
        
        # Counts of a feature in a category
        self.featCount = {}        
        
        # Counts of items in a category
        self.catCount = {}
        
        # Get features
        self.getFeatures = getFeatures
        
    # Increase the count of a feature in a category
    def incFeatCount(self, feat, cat):
        self.featCount.setdefault(feat, {})
        self.featCount[feat].setdefault(cat, 0);
        self.featCount[feat][cat] += 1;
        
    # Increase the count of a category
    def incCatCount(self, cat):
        self.catCount.setdefault(cat, 0)
        self.catCount[cat] += 1
        
    # Get the counts of a feature in a category
    def getFeatCount(self, feat, cat):
        if feat in self.featCount and cat in self.featCount[feat]:
            return float(self.featCount[feat][cat])
        
        return 0.0
    
    # Get the number of items in a category
    def getCatCount(self, cat):
        if cat in self.catCount:
            return float(self.catCount[cat])
        
        return 0
    
    # The total number of items
    def totalCatCount(self):
        return sum(self.catCount.values())
  
    # The list of all categories
    def catList(self):
        return self.catCount.keys()
    
    #Train the classifier
    def train(self, item, cat):
        features = self.getFeatures(item)
        
        # Increment the count for every feature with this category
        for feat in features:
            self.incFeatCount(feat, cat)
       
        # Increment the count for this category
        self.incCatCount(cat)
    
    # Pr(feature|category)     
    def featProb(self, feat, cat):
        if self.getCatCount(cat) == 0: 
            return 0
        
        # The probability of feature given category
        return self.getFeatCount(feat, cat) / self.getCatCount(cat)
    
    def weightedProb(self, feat, cat, featProb, weight=1.0, ap=0.5):  # ap = assumed probability
        
        # Calculate current probability
        basicProb = featProb(feat, cat)
        
        # Count the number of times this feature has appeared in all categories
        total = sum([self.getFeatCount(feat, c) for c in self.catList()])
        
        # Calculate the weighted average
        wp = ((weight * ap) + (total * basicProb)) / (weight + total)
       
        return wp 