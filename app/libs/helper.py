def is_isbn_or_key(word):
    """
    isbn13: 13个 0-9的数字
    isbn10： 10个 0-9的数字，还有一些 '-'符号
    判断 word 是否是 isbn还是字符
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
