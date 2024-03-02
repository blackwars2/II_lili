def del_first_word(text):
    text = text.split(' ')
    text.pop(0)
    text = ' '.join(text)
    return text