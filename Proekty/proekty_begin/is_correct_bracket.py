def is_correct_bracket(text):
    while '()' in text:
        text = text.replace("()", "")
    x = len(text)
    if x == 0:
        return True
    else:
        return False
txt = input()
print(is_correct_bracket(txt))