def get_num_words(text):
    word_list = []
    word_list = text.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")

def get_num_char(text):
    char_count = {}
    text = text.lower()
    word_list = text.split()
    for word in word_list:
        for i in range(0, len(word)):
            char_count[word[i]] = char_count.get(word[i], 0) + 1

    return char_count
    #for key in char_count:
    #   print(f"'{key}': {char_count[key]}")


def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    dict_list = []
    for key in dictionary:
        dict_list.append({"char": key, "num": dictionary[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list