def popular_words(text, words):
    dict_words = dict((key, value) for (key, value) in zip(words, len(words) * [0]))
    for i in text.split():
        if i.lower() in dict_words:
            dict_words[i.lower()] += 1
    return dict_words

# def popular_words(text, words):
#     lower_count = text.lower().split().count
#     return {word: lower_count(word) for word in words}

# def popular_words(text, words):
#     from collections import Counter
#     import re
#     count = Counter(re.split("[^a-z']+", text.lower()))
#     return {word: count[word] for word in words}

if __name__ == "__main__":
    text = '''When I was One
              I had just begun
              When I was Two
              I was nearly new
              '''
    words = ['i', 'was', 'three', 'near']
    print popular_words(text, words)