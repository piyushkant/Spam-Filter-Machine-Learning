#####################################################
#  Copyright (c) 2012 Piyush Kant                   #
#  See the file license.txt for copying permission  #
#####################################################

import re

def getwords(doc):
    splitter = re.compile('\\W*')
    
    # Split the words
    words = [s.lower() for s in splitter.split(doc) if len(s) > 2 and len(s) < 20]
    
    # Return the unique set of words only
    return dict([(w, 1) for w in words])

def initTrain(cl):
    cl.train('Nobody owns the water.', 'good')
    cl.train('the quick rabbit jumps fences', 'good')
    cl.train('buy pharmaceuticals now', 'bad')
    cl.train('make quick money at the online casino', 'bad')
    cl.train('the quick brown fox jumps', 'good')