
import settings
from features import build_features, FeatureFunction
from templates import *



a_templates = [WordLength_Template]
b_templates = [TagSequence_Template]

(a_features, b_features) = build_features(a_templates, b_templates)


print "a_features: ", a_features
print "b_features: ", b_features
#feature_function = FeatureFunction(a_features, b_features)


feature_function = FeatureFunction(a_features, b_features)

print "Caridinality of FeatureFunction: " + str(feature_function.cardinality())
