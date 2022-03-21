def spell(txt):
    if len(txt) == 1:
        print(txt[len(txt) - 1])
    else:
        print(txt[len(txt) - 1])
        txt = txt[:-1]
        return spell(txt)


txt = input('input text1: ')
spell(txt)
