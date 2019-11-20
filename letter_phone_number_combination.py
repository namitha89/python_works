


def rec(inp):

    if not inp:
        return []

    if len(inp) == 1:
        return list(inp[0])

    x = inp[0]
    del inp[0]

    out = []
    for i in x:
        for y in rec(inp):
            out.append(i + y)
    return out





x = {
    1: "abc",
    2: "def",
}

print(rec(x.values()))