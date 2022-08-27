


def compose(expression):
    arr = []
    text = ''
    for i in expression:
        if i.isdigit():
            text += i
        if not i.isdigit():
            if text:
                arr.append(text)
            arr.append(i)
            text = ''
    if text:
        arr.append(text)
    return arr


# print(decompose(['4', '*', '4', '+', '10']))
