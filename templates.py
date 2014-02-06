
import settings


class Template:
    total_funcs = 0
    def __init__(self):
    	return

    @staticmethod
    def cardinality():
        return Template.total_funcs

    def evaluate():
        return ""
    

class TagSequence_Template(Template):

    total_funcs = len(settings.tags) ** 2 
    def __init__(self, index):
        self.index = index

    @staticmethod
    def cardinality():
        return TagSequence_Template.total_funcs

    def evaluate(self, y_sequence, loc):
    	return 


class Wordlength_Template:
	total_funcs = 20
	@staticmethod
	def cardinality():
		return Wordlength_Template.total_funcs


