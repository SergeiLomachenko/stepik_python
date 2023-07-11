slovo = input()
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ser = "запретил букву"
word = slovo + ' ' + ser
for i in range(len(alphabet)):
    x = alphabet[i]
    if alphabet[i] in word:
        word = word + ' ' + alphabet[i]
        word = word.rstrip()
        print(word)
    word = word.replace(alphabet[i], '')
    word = word.replace('  ', ' ')
    word = word.lstrip()
    y = len(word)
    if y < 1:
        break
    word = word.rstrip()
