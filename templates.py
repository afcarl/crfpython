
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

    def evaluate(self, yt, ybefore, loc):
    	return


class WordLength_Template:
    total_funcs = 20

    def __init__(self, index):
        self.index = index

    @staticmethod
    def cardinality():
        return WordLength_Template.total_funcs

    def evaluate(self, x_sequence, loc):
        return


