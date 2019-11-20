x = """this is the world
we live in
and this is the people we live with"""

def word_count(x):
    x = " ".join(x.split())
    li = x.split(' ')
    out = {}
    for i in li:
        if i in out:
            out[i] +=1
        else:
            out[i] = 1
    return out



print(word_count(x))
