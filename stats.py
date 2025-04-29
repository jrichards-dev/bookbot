def get_num_words(text):
    word_list = []
    word_list = text.split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")

def get_num_char(text):
    char_count = {}
    text = text.lower()
    word_list = text.split()
    for word in word_list:
        for i in range(0, len(word)):
            char_count[word[i]] = char_count.get(word[i], 0) + 1

    for key in char_count:
        print(f"'{key}': {char_count[key]}")
