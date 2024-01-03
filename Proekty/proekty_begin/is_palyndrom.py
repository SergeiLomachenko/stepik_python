def is_palindrome(text):
    text = text.lower()
    sp = "".join(c for c in text if c.isalpha())
    sp1 = sp[::-1]
    if sp == sp1:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
