def valid_parentheses(expression):
    open_brackets = tuple('({[')
    closed_brackets = tuple(')}]')
    map = dict(zip(open_brackets,closed_brackets))
    print(map)
    queue = []

    for i in expression:
        if i in open_brackets:
            queue.append(map[i])
        elif i in closed_brackets:
            if not queue or i != queue.pop():
                return "unbalance"
    return "balanced"

string = "{[]{()}}"
print(string, "-", valid_parentheses(string))