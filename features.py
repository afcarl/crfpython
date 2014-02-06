import settings
import templates
import math



#####################################################
# J feature functions.
#####################################################

a_templates = []
b_templates = [TagSequence_Template]


a_features = []
b_features = []

(a_features, b_features) = build_features(a_templates, b_templates)

###############################################
#  take all a_templates, b_templates, return array of a featurefunction objects and b featurefunction objects
#  every a feature function object has an evaluate(x, i) function
#  every b feature function object has an evaluate(yi, ybeforei, i) function
###############################################
def build_features(a_templates, b_templates):

    a_features = []
    for template in a_templates:
        for i in xrange(template.cardinality()):
            a_features.append(template(i))

    for template in b_templates:
        for i in xrange(template.cardinality()):
            b_features.append(template(i))




def j_to_ab(j):

    a = int(math.ceil((j * 1.0) / (number_bs * 1.0 )))
    b = j % number_bs
    return (a,b)




a_featurefunctions = []

b_featurefunctions = []




a_templates = []
b_templates = []

def feature_function(j, y, x_seq, i):
    (a, b) = j_to_ab(j)

    return a_featurefunctions[a].evaluate(x,i) * b_featurefunctions[b].evaluate(y,i)



