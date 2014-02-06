

def test_a_template(template, index, x, i):
    a_function = template(index)
    return a_function.evaluate(x,i)


def test_b_template(template,index, yt, ybefore,i):
    b_function = template(index)
    return b_function.evaluate(yt, ybefore, i)
