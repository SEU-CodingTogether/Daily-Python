def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower().split()
    popular_words = dict(zip(words, [0 for _ in range(len(words))]))
    
    for item in text:
        if item in words:
            popular_words[item] += 1

    return popular_words


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete!")
text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
words = ['i', 'was', 'three', 'near']
print(zip(words, map(text.lower().split().count, words)))
