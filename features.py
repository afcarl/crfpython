import settings
import templates
import math



#####################################################
# J feature functions.
#####################################################





###############################################
#  take all a_templates, b_templates, return array of a featurefunction objects and b featurefunction objects
#  every a feature function object has an evaluate(x, i) function
#  every b feature function object has an evaluate(yi, ybeforei, i) function
###############################################
def build_features(a_templates, b_templates):

    a_features = []
    b_features = []
    for template in a_templates:
        for i in xrange(template.cardinality()):
            a_features.append(template(i))

    for template in b_templates:
        for i in xrange(template.cardinality()):
            b_features.append(template(i))

    return (a_features, b_features)


def j_to_ab(j, num_a, num_b):

    a = int(math.floor((j * 1.0) / (num_a * 1.0 )))
    b = j % num_b
    return (a,b)




a_featurefunctions = []

b_featurefunctions = []




a_templates = []
b_templates = []

class FeatureFunction:

    def __init__(self, a_features, b_features):
        self.a_features = a_features
        self.b_features = b_features

    def cardinality(self):
        return len(self.a_features) * len(self.b_features)

    def evaluate(self, j, x, y, i):
        (a, b) = j_to_ab(j, len(self.a_features), len(self.b_features))
        yt = y[i]
        if i == 0:
            ybefore = "START"
        else:
            ybefore = y[i-1]

        return self.a_features[a].evaluate(x,i) ** self.b_features[b].evaluate(yt, ybefore,i)





