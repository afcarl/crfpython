import templates

wtpl = templates.WordLength_Template(4)
assert wtpl.evaluate(["hello"], 0) == 1
