#####################################################
#  Copyright (c) 2012 Piyush Kant                   #
#  See the file license.txt for copying permission  #
#####################################################

import spamfilter
import classifier
import naivebayes
import fisher

############################Debugging####################################
cl = fisher.fisherclassifier(spamfilter.getwords)
spamfilter.initTrain(cl);
print cl.cProb('quick','good')